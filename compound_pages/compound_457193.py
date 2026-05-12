
import streamlit as st
import pandas as pd

st.set_page_config(page_title="DACTINOMYCIN", layout="wide")
st.title("DACTINOMYCIN")
st.markdown(f"PubChem Compound ID: [457193](https://pubchem.ncbi.nlm.nih.gov/compound/457193)")
st.markdown(f"IUPAC Name: 2-amino-4,6-dimethyl-3-oxo-1-N,9-N-bis[(3R,6S,7R,10S,16S)-7,11,14-trimethyl-2,5,9,12,15-pentaoxo-3,10-di(propan-2-yl)-8-oxa-1,4,11,14-tetrazabicyclo[14.3.0]nonadecan-6-yl]phenoxazine-1,9-dicarboxamide")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_457193.jpg", caption=f"SMILES: Cc1ccc(C(=O)NC2C(=O)NC(C(C)C)C(=O)N3CCCC3C(=O)N(C)CC(=O)N(C)C(C(C)C)C(=O)O[C@@H]2C)c2c1Oc1c(C)c(O)c(N)c(=C(O)N=C3C(=O)NC(C(C)C)C(=O)N4CCCC4C(=O)N(C)CC(=O)N(C)C(C(C)C)C(=O)O[C@@H]3C)c1=N2")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 457193) ]

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

    