
import streamlit as st
import pandas as pd

st.set_page_config(page_title="piperacillin", layout="wide")
st.title("piperacillin")
st.markdown(f"PubChem Compound ID: [43672](https://pubchem.ncbi.nlm.nih.gov/compound/43672)")
st.markdown(f"IUPAC Name: (2S,5R,6R)-6-[[(2R)-2-[(4-ethyl-2,3-dioxopiperazine-1-carbonyl)amino]-2-phenylacetyl]amino]-3,3-dimethyl-7-oxo-4-thia-1-azabicyclo[3.2.0]heptane-2-carboxylic acid")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_43672.jpg", caption=f"SMILES: CCN1CCN(C(=O)NC(C(=O)NC2C(=O)N3C(C(=O)O)C(C)(C)S[C@H]23)c2ccccc2)C(=O)C1=O")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 43672) ]

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

    