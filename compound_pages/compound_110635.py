
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Tadalafil", layout="wide")
st.title("Tadalafil")
st.markdown(f"PubChem Compound ID: [110635](https://pubchem.ncbi.nlm.nih.gov/compound/110635)")
st.markdown(f"IUPAC Name: (2R,8R)-2-(1,3-benzodioxol-5-yl)-6-methyl-3,6,17-triazatetracyclo[8.7.0.03,8.011,16]heptadeca-1(10),11,13,15-tetraene-4,7-dione")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_110635.jpg", caption=f"SMILES: CN1CC(=O)N2C(Cc3c([nH]c4ccccc34)[C@H]2c2ccc3c(c2)OCO3)C1=O")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 110635) ]

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

    