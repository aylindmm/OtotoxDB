
import streamlit as st
import pandas as pd

st.set_page_config(page_title="TERTOMOTIDE", layout="wide")
st.title("TERTOMOTIDE")
st.markdown(f"PubChem Compound ID: [56843375](https://pubchem.ncbi.nlm.nih.gov/compound/56843375)")
st.markdown(f"IUPAC Name: (2S)-6-amino-2-[[(2S)-1-[(2S,3S)-2-[[(2S)-2-[[(2S)-2-[[(2S)-2-[[(2S)-2-[[(2S)-2-[[(2S,3R)-2-[[(2S)-2-[[(2S)-2-[[(2S)-2-[[(2S)-1-[(2S)-2-[[(2S)-2-[[(2S)-2-amino-4-carboxybutanoyl]amino]propanoyl]amino]-5-(diaminomethylideneamino)pentanoyl]pyrrolidine-2-carbonyl]amino]propanoyl]amino]-4-methylpentanoyl]amino]-4-methylpentanoyl]amino]-3-hydroxybutanoyl]amino]-3-hydroxypropanoyl]amino]-5-(diaminomethylideneamino)pentanoyl]amino]-4-methylpentanoyl]amino]-5-(diaminomethylideneamino)pentanoyl]amino]-3-phenylpropanoyl]amino]-3-methylpentanoyl]pyrrolidine-2-carbonyl]amino]hexanoic acid")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_56843375.jpg", caption=f"SMILES: CC[C@H](C)C(NC(=O)C(Cc1ccccc1)NC(=O)C(CCCN=C(N)N)NC(=O)C(CC(C)C)NC(=O)C(CCCN=C(N)N)NC(=O)C(CO)NC(=O)C(NC(=O)C(CC(C)C)NC(=O)C(CC(C)C)NC(=O)C(C)NC(=O)C1CCCN1C(=O)C(CCCN=C(N)N)NC(=O)C(C)NC(=O)C(N)CCC(=O)O)[C@@H](C)O)C(=O)N1CCCC1C(=O)NC(CCCCN)C(=O)O")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 56843375) ]

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

    