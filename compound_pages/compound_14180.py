
import streamlit as st
import pandas as pd

st.set_page_config(page_title="1094-61-7", layout="wide")
st.title("1094-61-7")
st.markdown(f"PubChem Compound ID: [14180](https://pubchem.ncbi.nlm.nih.gov/compound/14180)")
st.markdown(f"IUPAC Name: [(2R,3S,4R,5R)-5-(3-carbamoylpyridin-1-ium-1-yl)-3,4-dihydroxyoxolan-2-yl]methyl hydrogen phosphate")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_14180.jpg", caption=f"SMILES: NC(=O)c1ccc[n+]([C@@H]2O[C@H](COP(=O)([O-])O)[C@@H](O)[C@H]2O)c1")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 14180) ]

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

    