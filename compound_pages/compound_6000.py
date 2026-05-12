
import streamlit as st
import pandas as pd

st.set_page_config(page_title="tubocurarine", layout="wide")
st.title("tubocurarine")
st.markdown(f"PubChem Compound ID: [6000](https://pubchem.ncbi.nlm.nih.gov/compound/6000)")
st.markdown(f"IUPAC Name: (1S,16R)-10,25-dimethoxy-15,15,30-trimethyl-7,23-dioxa-30-aza-15-azoniaheptacyclo[22.6.2.23,6.18,12.118,22.027,31.016,34]hexatriaconta-3(36),4,6(35),8(34),9,11,18(33),19,21,24,26,31-dodecaene-9,21-diol")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_6000.jpg", caption=f"SMILES: COc1cc2c3cc1Oc1cc(ccc1O)C[C@@H]1c4c(cc(OC)c(O)c4Oc4ccc(cc4)C[C@@H]3N(C)CC2)CC[N+]1(C)C")

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

    