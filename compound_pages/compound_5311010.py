
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Atosiban", layout="wide")
st.title("Atosiban")
st.markdown(f"PubChem Compound ID: [5311010](https://pubchem.ncbi.nlm.nih.gov/compound/5311010)")
st.markdown(f"IUPAC Name: (2S)-N-[(2S)-5-amino-1-[(2-amino-2-oxoethyl)amino]-1-oxopentan-2-yl]-1-[(4R,7S,10S,13S,16R)-7-(2-amino-2-oxoethyl)-13-[(2S)-butan-2-yl]-16-[(4-ethoxyphenyl)methyl]-10-[(1R)-1-hydroxyethyl]-6,9,12,15,18-pentaoxo-1,2-dithia-5,8,11,14,17-pentazacycloicosane-4-carbonyl]pyrrolidine-2-carboxamide")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_5311010.jpg", caption=f"SMILES: CCOc1ccc(CC2NC(=O)CCSSCC(C(=O)N3CCCC3C(=O)NC(CCCN)C(=O)NCC(N)=O)NC(=O)C(CC(N)=O)NC(=O)C([C@@H](C)O)NC(=O)C([C@@H](C)CC)NC2=O)cc1")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 5311010) ]

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

    