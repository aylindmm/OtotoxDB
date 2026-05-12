
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Melanin", layout="wide")
st.title("Melanin")
st.markdown(f"PubChem Compound ID: [6325610](https://pubchem.ncbi.nlm.nih.gov/compound/6325610)")
st.markdown(f"IUPAC Name: 6,14-dimethyl-4,12-diazapentacyclo[8.6.1.12,5.013,17.09,18]octadeca-1(17),2,5,9(18),10,13-hexaene-7,8,15,16-tetrone")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_6325610.jpg", caption=f"SMILES: Cc1c(=O)c(=O)c2c3c[nH]c4c(C)c(=O)c(=O)c(c5c[nH]c1c52)c43")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 6325610) ]

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

    