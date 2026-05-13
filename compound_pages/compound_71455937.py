
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Elx-02", layout="wide")
st.title("Elx-02")
# Display the image in Streamlit
st.image(f"compound_structures/compound_71455937.jpg", width=300)
st.markdown(f"PubChem Compound ID: [71455937](https://pubchem.ncbi.nlm.nih.gov/compound/71455937)")
st.markdown(f"IUPAC Name: (2R,3S,4R,5R,6S)-5-amino-6-[(1R,2R,3S,4R,6S)-4,6-diamino-2-[(2S,3R,4S,5R)-5-[(1R)-1-aminoethyl]-3,4-dihydroxyoxolan-2-yl]oxy-3-hydroxycyclohexyl]oxy-2-[(1R)-1-hydroxyethyl]oxane-3,4-diol")
st.markdown(f"Score: 0.0134498991257566")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 71455937) ]


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

    