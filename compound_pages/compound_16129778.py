
import streamlit as st
import pandas as pd

st.set_page_config(page_title="TANNIC ACID", layout="wide")
st.title("TANNIC ACID")
st.markdown(f"PubChem Compound ID: [16129778](https://pubchem.ncbi.nlm.nih.gov/compound/16129778)")
st.markdown(f"IUPAC Name: [2,3-dihydroxy-5-[[(2R,3R,4S,5R,6S)-3,4,5,6-tetrakis[[3,4-dihydroxy-5-(3,4,5-trihydroxybenzoyl)oxybenzoyl]oxy]oxan-2-yl]methoxycarbonyl]phenyl] 3,4,5-trihydroxybenzoate")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_16129778.jpg", caption=f"SMILES: O=C(OC[C@H]1O[C@@H](OC(=O)c2cc(O)c(O)c(OC(=O)c3cc(O)c(O)c(O)c3)c2)[C@H](OC(=O)c2cc(O)c(O)c(OC(=O)c3cc(O)c(O)c(O)c3)c2)[C@@H](OC(=O)c2cc(O)c(O)c(OC(=O)c3cc(O)c(O)c(O)c3)c2)[C@@H]1OC(=O)c1cc(O)c(O)c(OC(=O)c2cc(O)c(O)c(O)c2)c1)c1cc(O)c(O)c(OC(=O)c2cc(O)c(O)c(O)c2)c1")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 16129778) ]

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

    