
import streamlit as st
import pandas as pd

st.set_page_config(page_title="pravastatin", layout="wide")
st.title("pravastatin")
st.markdown(f"PubChem Compound ID: [54687](https://pubchem.ncbi.nlm.nih.gov/compound/54687)")
st.markdown(f"IUPAC Name: (3R,5R)-7-[(1S,2S,6S,8S,8aR)-6-hydroxy-2-methyl-8-[(2S)-2-methylbutanoyl]oxy-1,2,6,7,8,8a-hexahydronaphthalen-1-yl]-3,5-dihydroxyheptanoic acid")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_54687.jpg", caption=f"SMILES: CCC(C)C(=O)O[C@H]1C[C@H](O)C=C2C=C[C@H](C)[C@H](CC[C@@H](O)C[C@@H](O)CC(=O)O)[C@H]21")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 54687) ]

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

    