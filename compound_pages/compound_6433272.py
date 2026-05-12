
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Stamycin", layout="wide")
st.title("Stamycin")
st.markdown(f"PubChem Compound ID: [6433272](https://pubchem.ncbi.nlm.nih.gov/compound/6433272)")
st.markdown(f"IUPAC Name: (1S,15S,16R,17R,18S,19E,21E,25E,27E,29E,31E)-33-[(2S,3S,4S,5S,6R)-4-amino-3,5-dihydroxy-6-methyloxan-2-yl]oxy-1,3,4,7,9,11,17,37-octahydroxy-15,16,18-trimethyl-13-oxo-14,39-dioxabicyclo[33.3.1]nonatriaconta-19,21,25,27,29,31-hexaene-36-carboxylic acid")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_6433272.jpg", caption=f"SMILES: C[C@@H]1[C@H](O)[C@@H](C)/C=C/C=C/CC/C=C/C=C/C=C/C=C/C(O[C@H]2O[C@H](C)[C@@H](O)[C@H](N)[C@@H]2O)CC2O[C@](O)(CC(O)C(O)CCC(O)CC(O)CC(O)CC(=O)O[C@H]1C)CC(O)C2C(=O)O")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 6433272) ]

# Convert dataframe to CSV
csv = df_filtered.to_csv(index=False, sep='\t').encode('utf-8')

st.download_button(
    label="Download data as TSV",
    data=csv,
    file_name='articles.tsv',
    mime='text/tsv',
)


df_filtered['PMID'] = df_filtered['PMID'].apply(lambda x: f"https://pubmed.ncbi.nlm.nih.gov/{x}/")  

for variable in df_filtered['variable'].unique():
    st.markdown(f"**{variable}**")
    source_df = df_filtered[df_filtered['variable'] == variable]
    st.dataframe(
        source_df[["PMID", "Title"]].rename(columns={"PMID": "PubMed ID", "Title": "Title"}),
        use_container_width=True,
        column_config={
            "PubMed ID": st.column_config.LinkColumn("PubMed ID", display_text="https://pubmed.ncbi.nlm.nih.gov/(.*?)/"),
            "Title": st.column_config.TextColumn("Title"),
        },
        hide_index=True,
    )


if st.button("Back"):
    st.switch_page("pages/1_Home.py")

    