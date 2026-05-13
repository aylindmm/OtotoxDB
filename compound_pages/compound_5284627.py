
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Topiramate", layout="wide")
st.title("Topiramate")
# Display the image in Streamlit
st.image(f"compound_structures/compound_5284627.jpg", width=300)
st.markdown(f"PubChem Compound ID: [5284627](https://pubchem.ncbi.nlm.nih.gov/compound/5284627)")
st.markdown(f"IUPAC Name: [(1R,2S,6S,9R)-4,4,11,11-tetramethyl-3,5,7,10,12-pentaoxatricyclo[7.3.0.02,6]dodecan-6-yl]methyl sulfamate")
st.markdown(f"Score: 0.0134498991257566")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 5284627) ]


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

    