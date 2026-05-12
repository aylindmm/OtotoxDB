
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Octreotide", layout="wide")
st.title("Octreotide")
st.markdown(f"PubChem Compound ID: [448601](https://pubchem.ncbi.nlm.nih.gov/compound/448601)")
st.markdown(f"IUPAC Name: (4R,7S,10S,13R,16S,19R)-10-(4-aminobutyl)-19-[[(2R)-2-amino-3-phenylpropanoyl]amino]-16-benzyl-N-[(2R,3R)-1,3-dihydroxybutan-2-yl]-7-[(1R)-1-hydroxyethyl]-13-(1H-indol-3-ylmethyl)-6,9,12,15,18-pentaoxo-1,2-dithia-5,8,11,14,17-pentazacycloicosane-4-carboxamide")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_448601.jpg", width=400)

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 448601) ]

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

    