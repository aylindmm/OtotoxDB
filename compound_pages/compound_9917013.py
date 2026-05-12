
import streamlit as st
import pandas as pd

st.set_page_config(page_title="CEP-1347", layout="wide")
st.title("CEP-1347")
st.markdown(f"PubChem Compound ID: [9917013](https://pubchem.ncbi.nlm.nih.gov/compound/9917013)")
st.markdown(f"IUPAC Name: methyl (15S,16R,18R)-10,23-bis(ethylsulfanylmethyl)-16-hydroxy-15-methyl-3-oxo-28-oxa-4,14,19-triazaoctacyclo[12.11.2.115,18.02,6.07,27.08,13.019,26.020,25]octacosa-1,6,8(13),9,11,20(25),21,23,26-nonaene-16-carboxylate")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_9917013.jpg", caption=f"SMILES: CCSCc1ccc2c(c1)c1c3c(c4c5cc(CSCC)ccc5n5c4c1n2[C@H]1C[C@](O)(C(=O)OC)[C@]5(C)O1)CNC3=O")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 9917013) ]

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

    