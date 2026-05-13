
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Cyclodextrin", layout="wide")
st.title("Cyclodextrin")
# Display the image in Streamlit
st.image(f"compound_structures/compound_320760.jpg", width=300)
st.markdown(f"PubChem Compound ID: [320760](https://pubchem.ncbi.nlm.nih.gov/compound/320760)")
st.markdown(f"IUPAC Name: 5,10,15,20,25,30-hexakis(hydroxymethyl)-2,4,7,9,12,14,17,19,22,24,27,29-dodecaoxaheptacyclo[26.2.2.23,6.28,11.213,16.218,21.223,26]dotetracontane-31,32,33,34,35,36,37,38,39,40,41,42-dodecol")
st.markdown(f"Score: 0.0134498991257566")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 320760) ]


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

    