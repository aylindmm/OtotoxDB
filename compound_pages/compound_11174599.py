
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Tetrodotoxin", layout="wide")
st.title("Tetrodotoxin")
# Display the image in Streamlit
st.image(f"compound_structures/compound_11174599.jpg", width=300)
st.markdown(f"PubChem Compound ID: [11174599](https://pubchem.ncbi.nlm.nih.gov/compound/11174599)")
st.markdown(f"IUPAC Name: (1R,5R,6R,7R,9S,11S,12S,13S,14S)-3-amino-14-(hydroxymethyl)-8,10-dioxa-2,4-diazatetracyclo[7.3.1.17,11.01,6]tetradec-3-ene-5,9,12,13,14-pentol")
st.markdown(f"Score: 0.0134498991257566")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 11174599) ]


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

    