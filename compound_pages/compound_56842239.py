
import streamlit as st
import pandas as pd

st.set_page_config(page_title="n-3 PUFA", layout="wide")
st.title("n-3 PUFA")
st.markdown(f"PubChem Compound ID: [56842239](https://pubchem.ncbi.nlm.nih.gov/compound/56842239)")
st.markdown(f"IUPAC Name: (4Z,7Z,10Z,13Z,16Z,19Z)-docosa-4,7,10,13,16,19-hexaenoic acid;(5Z,8Z,11Z,14Z,17Z)-icosa-5,8,11,14,17-pentaenoic acid;(9Z,12Z,15Z)-octadeca-9,12,15-trienoic acid")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_56842239.jpg", caption=f"SMILES: CC/C=C\C/C=C\C/C=C\C/C=C\C/C=C\C/C=C\CCC(=O)O.CC/C=C\C/C=C\C/C=C\C/C=C\C/C=C\CCCC(=O)O.CC/C=C\C/C=C\C/C=C\CCCCCCCC(=O)O")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 56842239) ]

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

    