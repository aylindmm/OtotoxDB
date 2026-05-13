
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Antibiotics", layout="wide")
st.title("Antibiotics")
# Display the image in Streamlit
st.image(f"compound_structures/compound_46874763.jpg", width=300)
st.markdown(f"PubChem Compound ID: [46874763](https://pubchem.ncbi.nlm.nih.gov/compound/46874763)")
st.markdown(f"IUPAC Name: 2-[[[(1R)-1-[[(2R)-2-[3-acetamido-2-[[[(2R,3S,4R)-3,4-dihydroxy-5-(5-iodo-2,4-dioxopyrimidin-1-yl)oxolan-2-yl]methoxy-hydroxyphosphoryl]oxy-hydroxyphosphoryl]oxy-5-hydroxy-6-(hydroxymethyl)oxan-4-yl]oxypropanoyl]amino]ethyl]-hydroxyphosphoryl]methyl]pentanedioic acid")
st.markdown(f"Score: 0.121049092131809")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 46874763) ]


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

    