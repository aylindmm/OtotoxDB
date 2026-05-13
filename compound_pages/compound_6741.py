
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Methylprednisolone", layout="wide")
st.title("Methylprednisolone")
# Display the image in Streamlit
st.image(f"compound_structures/compound_6741.jpg", width=300)
st.markdown(f"PubChem Compound ID: [6741](https://pubchem.ncbi.nlm.nih.gov/compound/6741)")
st.markdown(f"IUPAC Name: (6S,8S,9S,10R,11S,13S,14S,17R)-11,17-dihydroxy-17-(2-hydroxyacetyl)-6,10,13-trimethyl-7,8,9,11,12,14,15,16-octahydro-6H-cyclopenta[a]phenanthren-3-one")
st.markdown(f"Score: -0.121049092131809")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 6741) ]


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

    