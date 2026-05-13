
import streamlit as st
import pandas as pd

st.set_page_config(page_title="2-naphthacenecarboxamide, 4-(dimethylamino)-1,4,4a,5,5a,6,11,12a-octahydro-3,5,6,10,12,12a-hexahydroxy-6-methyl-1,11-dioxo-, hydrochloride (1:1), (4s,4ar,5s,5ar,6s,12as)-", layout="wide")
st.title("2-naphthacenecarboxamide, 4-(dimethylamino)-1,4,4a,5,5a,6,11,12a-octahydro-3,5,6,10,12,12a-hexahydroxy-6-methyl-1,11-dioxo-, hydrochloride (1:1), (4s,4ar,5s,5ar,6s,12as)-")
# Display the image in Streamlit
st.image(f"compound_structures/compound_54680782.jpg", width=300)
st.markdown(f"PubChem Compound ID: [54680782](https://pubchem.ncbi.nlm.nih.gov/compound/54680782)")
st.markdown(f"IUPAC Name: (4S,4aR,5S,5aR,6S,12aR)-4-(dimethylamino)-1,5,6,10,11,12a-hexahydroxy-6-methyl-3,12-dioxo-4,4a,5,5a-tetrahydrotetracene-2-carboxamide;hydrochloride")
st.markdown(f"Score: 0.0134498991257566")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 54680782) ]


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

    