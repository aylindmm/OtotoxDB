
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Bilirubin", layout="wide")
st.title("Bilirubin")
# Display the image in Streamlit
st.image(f"compound_structures/compound_5280352.jpg", width=300)
st.markdown(f"PubChem Compound ID: [5280352](https://pubchem.ncbi.nlm.nih.gov/compound/5280352)")
st.markdown(f"IUPAC Name: 3-[2-[[3-(2-carboxyethyl)-5-[(Z)-(3-ethenyl-4-methyl-5-oxopyrrol-2-ylidene)methyl]-4-methyl-1H-pyrrol-2-yl]methyl]-5-[(Z)-(4-ethenyl-3-methyl-5-oxopyrrol-2-ylidene)methyl]-4-methyl-1H-pyrrol-3-yl]propanoic acid")
st.markdown(f"Score: -0.0134498991257566")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 5280352) ]


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

    