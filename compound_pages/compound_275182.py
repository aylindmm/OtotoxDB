
import streamlit as st
import pandas as pd

st.set_page_config(page_title="BERBAMINE", layout="wide")
st.title("BERBAMINE")
st.markdown(f"PubChem Compound ID: [275182](https://pubchem.ncbi.nlm.nih.gov/compound/275182)")
st.markdown(f"IUPAC Name: (1S,14R)-20,21,25-trimethoxy-15,30-dimethyl-7,23-dioxa-15,30-diazaheptacyclo[22.6.2.23,6.18,12.114,18.027,31.022,33]hexatriaconta-3(36),4,6(35),8,10,12(34),18,20,22(33),24,26,31-dodecaen-9-ol")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_275182.jpg", caption=f"SMILES: COc1cc2c3cc1Oc1c(OC)c(OC)cc4c1[C@@H](Cc1ccc(O)c(c1)Oc1ccc(cc1)C[C@@H]3N(C)CC2)N(C)CC4")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 275182) ]

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

    