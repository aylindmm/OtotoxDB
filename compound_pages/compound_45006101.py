
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Refchem:1093319", layout="wide")
st.title("Refchem:1093319")
# Display the image in Streamlit
st.image(f"compound_structures/compound_45006101.jpg", width=300)
st.markdown(f"PubChem Compound ID: [45006101](https://pubchem.ncbi.nlm.nih.gov/compound/45006101)")
st.markdown(f"IUPAC Name: (2R,3R,4S,5S,6R)-2-[[(1S,3R,6S,9S,12S,14S,15R,16R)-14-hydroxy-15-[(2R,5S)-5-(2-hydroxypropan-2-yl)-2-methyloxolan-2-yl]-7,7,12,16-tetramethyl-6-[(2S,3R,4S,5R)-3,4,5-trihydroxyoxan-2-yl]oxy-9-pentacyclo[9.7.0.01,3.03,8.012,16]octadecanyl]oxy]-6-(hydroxymethyl)oxane-3,4,5-triol")
st.markdown(f"Score: -0.0134498991257566")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 45006101) ]


df_filtered['PMID'] = df_filtered['PMID'].apply(lambda x: f"https://pubmed.ncbi.nlm.nih.gov/{x}/")  

variable_labels = {
    "ototoxic_drugs": "Ototoxic Reports",
    "otoprotective_drugs": "Otoprotective Reports",
}


for variable in df_filtered['variable'].unique():

    label = variable_labels.get(variable, variable)  # falls back to raw name if not in dict
    st.markdown(f"**{label}**")
    source_df = df_filtered[df_filtered['variable'] == variable]
    st.dataframe(
        source_df[["PMID", "Title", "Year"]].rename(columns={"PMID": "PubMed ID", "Title": "Title", "Year": "Year"}),
        use_container_width=True,
        column_config={
            "PubMed ID": st.column_config.LinkColumn("PubMed ID", display_text="https://pubmed.ncbi.nlm.nih.gov/(.*?)/"),
            "Title": st.column_config.TextColumn("Title"),
        },
        hide_index=True,
    )


if st.button("Back"):
    st.switch_page("pages/1_Home.py")

    