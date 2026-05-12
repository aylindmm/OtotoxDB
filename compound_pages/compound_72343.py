
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Hernandezine", layout="wide")
st.title("Hernandezine")
st.markdown(f"PubChem Compound ID: [72343](https://pubchem.ncbi.nlm.nih.gov/compound/72343)")
st.markdown(f"IUPAC Name: (1S,14S)-9,19,20,21,25-pentamethoxy-15,30-dimethyl-7,23-dioxa-15,30-diazaheptacyclo[22.6.2.23,6.18,12.114,18.027,31.022,33]hexatriaconta-3(36),4,6(35),8,10,12(34),18(33),19,21,24,26,31-dodecaene")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_72343.jpg", caption=f"SMILES: COc1ccc2cc1Oc1ccc(cc1)C[C@H]1c3cc(c(OC)cc3CCN1C)Oc1c(OC)c(OC)c(OC)c3c1[C@H](C2)N(C)CC3")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 72343) ]

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

    