
import streamlit as st
import pandas as pd

st.set_page_config(page_title="bilirubin", layout="wide")
st.title("bilirubin")
st.markdown(f"PubChem Compound ID: [5280352](https://pubchem.ncbi.nlm.nih.gov/compound/5280352)")
st.markdown(f"IUPAC Name: 3-[2-[[3-(2-carboxyethyl)-5-[(Z)-(3-ethenyl-4-methyl-5-oxopyrrol-2-ylidene)methyl]-4-methyl-1H-pyrrol-2-yl]methyl]-5-[(Z)-(4-ethenyl-3-methyl-5-oxopyrrol-2-ylidene)methyl]-4-methyl-1H-pyrrol-3-yl]propanoic acid")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_5280352.jpg", caption=f"SMILES: C=CC1=C(C)C(Cc2[nH]c(Cc3[nH]c(C=c4[nH]c(O)c(C)c4=CC)c(C)c3C=CC(=O)O)c(CCC(=O)O)c2C)=NC1=O")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 5280352) ]

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

    