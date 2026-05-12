
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Somatostatin", layout="wide")
st.title("Somatostatin")
st.markdown(f"PubChem Compound ID: [16129706](https://pubchem.ncbi.nlm.nih.gov/compound/16129706)")
st.markdown(f"IUPAC Name: (4R,7S,10S,13S,16S,19S,22S,25S,28S,31S,34S,37R)-19,34-bis(4-aminobutyl)-31-(2-amino-2-oxoethyl)-37-[[2-[[(2S)-2-aminopropanoyl]amino]acetyl]amino]-13,25,28-tribenzyl-10,16-bis[(1R)-1-hydroxyethyl]-7-(hydroxymethyl)-22-(1H-indol-3-ylmethyl)-6,9,12,15,18,21,24,27,30,33,36-undecaoxo-1,2-dithia-5,8,11,14,17,20,23,26,29,32,35-undecazacyclooctatriacontane-4-carboxylic acid")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_16129706.jpg", width=400)

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 16129706) ]

# Convert dataframe to CSV
csv = df_filtered.to_csv(index=False, sep='\t').encode('utf-8')

st.download_button(
    label="Download data as TSV",
    data=csv,
    file_name='articles.tsv',
    mime='text/tsv',
)


df_filtered['PMID'] = df_filtered['PMID'].apply(lambda x: f"https://pubmed.ncbi.nlm.nih.gov/{x}/")  

for variable in df_filtered['variable'].unique():
    st.markdown(f"**{variable}**")
    source_df = df_filtered[df_filtered['variable'] == variable]
    st.dataframe(
        source_df[["PMID", "Title"]].rename(columns={"PMID": "PubMed ID", "Title": "Title"}),
        use_container_width=True,
        column_config={
            "PubMed ID": st.column_config.LinkColumn("PubMed ID", display_text="https://pubmed.ncbi.nlm.nih.gov/(.*?)/"),
            "Title": st.column_config.TextColumn("Title"),
        },
        hide_index=True,
    )


if st.button("Back"):
    st.switch_page("pages/1_Home.py")

    