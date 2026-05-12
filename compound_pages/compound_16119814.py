
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Caspofungin", layout="wide")
st.title("Caspofungin")
st.markdown(f"PubChem Compound ID: [16119814](https://pubchem.ncbi.nlm.nih.gov/compound/16119814)")
st.markdown(f"IUPAC Name: (10R,12S)-N-[(3S,6S,9S,11R,15S,18S,20R,21S,24S,25S)-21-(2-aminoethylamino)-3-[(1R)-3-amino-1-hydroxypropyl]-6-[(1S,2S)-1,2-dihydroxy-2-(4-hydroxyphenyl)ethyl]-11,20,25-trihydroxy-15-[(1R)-1-hydroxyethyl]-2,5,8,14,17,23-hexaoxo-1,4,7,13,16,22-hexazatricyclo[22.3.0.09,13]heptacosan-18-yl]-10,12-dimethyltetradecanamide")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_16119814.jpg", caption=f"SMILES: CC[C@H](C)C[C@H](C)CCCCCCCCC(=O)NC1C[C@@H](O)[C@@H](NCCN)NC(=O)C2[C@@H](O)CCN2C(=O)C([C@H](O)CCN)NC(=O)C([C@H](O)[C@@H](O)c2ccc(O)cc2)NC(=O)C2C[C@@H](O)CN2C(=O)C([C@@H](C)O)NC1=O")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 16119814) ]

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

    