
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Celastrol", layout="wide")
st.title("Celastrol")
# Display the image in Streamlit
st.image(f"compound_structures/compound_122724.jpg", width=300)
st.markdown(f"PubChem Compound ID: [122724](https://pubchem.ncbi.nlm.nih.gov/compound/122724)")
st.markdown(f"IUPAC Name: (2R,4aS,6aR,6aS,14aS,14bR)-10-hydroxy-2,4a,6a,6a,9,14a-hexamethyl-11-oxo-1,3,4,5,6,13,14,14b-octahydropicene-2-carboxylic acid")
st.markdown(f"Score: -0.0268997982515131")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 122724) ]


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

    