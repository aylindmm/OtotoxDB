
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Actinomycin 7", layout="wide")
st.title("Actinomycin 7")
# Display the image in Streamlit
st.image(f"compound_structures/compound_44415057.jpg", width=300)
st.markdown(f"PubChem Compound ID: [44415057](https://pubchem.ncbi.nlm.nih.gov/compound/44415057)")
st.markdown(f"IUPAC Name: 2-amino-4,6-dimethyl-3-oxo-1-N,9-N-bis[(3R,6S,7S,10S,16S)-7,11,14-trimethyl-2,5,9,12,15-pentaoxo-3,10-di(propan-2-yl)-8-oxa-1,4,11,14-tetrazabicyclo[14.3.0]nonadecan-6-yl]phenoxazine-1,9-dicarboxamide")
st.markdown(f"Score: 0.0134498991257566")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 44415057) ]


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

    