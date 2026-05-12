
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dihydrostreptomycin sulfate", layout="wide")
st.title("Dihydrostreptomycin sulfate")
st.markdown(f"PubChem Compound ID: [21653](https://pubchem.ncbi.nlm.nih.gov/compound/21653)")
st.markdown(f"IUPAC Name: bis(2-[(1R,2R,3S,4R,5R,6S)-3-(diaminomethylideneamino)-4-[(2R,3R,4R,5S)-3-[(2S,3S,4S,5R,6S)-4,5-dihydroxy-6-(hydroxymethyl)-3-(methylamino)oxan-2-yl]oxy-4-hydroxy-4-(hydroxymethyl)-5-methyloxolan-2-yl]oxy-2,5,6-trihydroxycyclohexyl]guanidine);sulfuric acid")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_21653.jpg", width=400)

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 21653) ]

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

    