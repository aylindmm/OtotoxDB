
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Tubocurarine", layout="wide")
st.title("Tubocurarine")
# Display the image in Streamlit
st.image(f"compound_structures/compound_6000.jpg", width=300)
st.markdown(f"PubChem Compound ID: [6000](https://pubchem.ncbi.nlm.nih.gov/compound/6000)")
st.markdown(f"IUPAC Name: (1S,16R)-10,25-dimethoxy-15,15,30-trimethyl-7,23-dioxa-30-aza-15-azoniaheptacyclo[22.6.2.23,6.18,12.118,22.027,31.016,34]hexatriaconta-3(36),4,6(35),8(34),9,11,18(33),19,21,24,26,31-dodecaene-9,21-diol")
st.markdown(f"Score: -0.0134498991257566")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 6000) ]

# Convert dataframe to CSV
csv = df_filtered.to_csv(index=False, sep='\t').encode('utf-8')

st.download_button(
    label="Download data as TSV",
    data=csv,
    file_name='articles.tsv',
    mime='text/tsv',
)


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

    