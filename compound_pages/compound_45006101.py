
import streamlit as st
import pandas as pd

st.set_page_config(page_title="RefChem:1093319", layout="wide")
st.title("RefChem:1093319")
st.markdown(f"PubChem Compound ID: [45006101](https://pubchem.ncbi.nlm.nih.gov/compound/45006101)")
st.markdown(f"IUPAC Name: (2R,3R,4S,5S,6R)-2-[[(1S,3R,6S,9S,12S,14S,15R,16R)-14-hydroxy-15-[(2R,5S)-5-(2-hydroxypropan-2-yl)-2-methyloxolan-2-yl]-7,7,12,16-tetramethyl-6-[(2S,3R,4S,5R)-3,4,5-trihydroxyoxan-2-yl]oxy-9-pentacyclo[9.7.0.01,3.03,8.012,16]octadecanyl]oxy]-6-(hydroxymethyl)oxane-3,4,5-triol")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_45006101.jpg", caption=f"SMILES: CC(C)(O)[C@@H]1CC[C@](C)([C@H]2[C@@H](O)C[C@@]3(C)C4C[C@H](O[C@@H]5O[C@H](CO)[C@@H](O)[C@H](O)[C@H]5O)C5C(C)(C)[C@@H](O[C@@H]6OC[C@@H](O)[C@H](O)[C@H]6O)CC[C@@]56C[C@@]46CC[C@]23C)O1")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 45006101) ]

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

    