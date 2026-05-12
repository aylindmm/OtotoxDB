
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Cefquinome", layout="wide")
st.title("Cefquinome")
st.markdown(f"PubChem Compound ID: [5464355](https://pubchem.ncbi.nlm.nih.gov/compound/5464355)")
st.markdown(f"IUPAC Name: (6R,7R)-7-[[(2Z)-2-(2-amino-1,3-thiazol-4-yl)-2-methoxyiminoacetyl]amino]-8-oxo-3-(5,6,7,8-tetrahydroquinolin-1-ium-1-ylmethyl)-5-thia-1-azabicyclo[4.2.0]oct-2-ene-2-carboxylate")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_5464355.jpg", caption=f"SMILES: CON=C(C(=O)NC1C(=O)N2C(C(=O)[O-])=C(C[n+]3cccc4c3CCCC4)CS[C@H]12)c1csc(N)n1")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 5464355) ]

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

    