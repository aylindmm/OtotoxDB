
import streamlit as st
import pandas as pd

st.set_page_config(page_title="GC-1008", layout="wide")
st.title("GC-1008")
st.markdown(f"PubChem Compound ID: [56842206](https://pubchem.ncbi.nlm.nih.gov/compound/56842206)")
st.markdown(f"IUPAC Name: (2S)-2-[[(2S)-2-[[(2S)-2-[[(2S)-2-[[(2S)-2-[[(2S)-2-[[(2S)-2-[[(2S)-1-[(2S)-1-[(2S)-2-[[(2S)-2-[[(2S)-2-[[(2S)-2-[[(2S)-2-[[(2S)-2-[[(2S)-4-amino-2-[[(2S,3R)-2-[[(2S)-1-[(2S)-2-[[(2S)-2-[[(2S)-2-[[(2S,3R)-2-[[(2S)-2-[[(2S)-2-[[2-[[(2S)-2-[[(2S)-2-[[(2S)-4-amino-2-[[(2S)-2-[[(2S,3R)-2-[[(2S)-2-[[(2S,3R)-2-[[(2S)-2-[[2-[[(2S)-2-[[(2S)-2-[[(2S)-5-amino-2-[[(2S,3S)-2-[[(2S)-2-[[(2S)-2-[[(2S)-2-[[(2S)-2-[[(2S)-2-amino-4-methylsulfanylbutanoyl]amino]-4-methylpentanoyl]amino]-3-methylbutanoyl]amino]propanoyl]amino]propanoyl]amino]-3-methylpentanoyl]amino]-5-oxopentanoyl]amino]-3-hydroxypropanoyl]amino]propanoyl]amino]acetyl]amino]-4-methylpentanoyl]amino]-3-hydroxybutanoyl]amino]-4-carboxybutanoyl]amino]-3-hydroxybutanoyl]amino]-4-methylpentanoyl]amino]-4-oxobutanoyl]amino]-5-carbamimidamidopentanoyl]amino]-4-carboxybutanoyl]amino]acetyl]amino]-3-methylbutanoyl]amino]-3-(4-hydroxyphenyl)propanoyl]amino]-3-hydroxybutanoyl]amino]-3-methylbutanoyl]amino]-3-phenylpropanoyl]amino]propanoyl]pyrrolidine-2-carbonyl]amino]-3-hydroxybutanoyl]amino]-4-oxobutanoyl]amino]-4-carboxybutanoyl]amino]propanoyl]amino]-3-phenylpropanoyl]amino]-5-carbamimidamidopentanoyl]amino]propanoyl]amino]-4-methylpentanoyl]pyrrolidine-2-carbonyl]pyrrolidine-2-carbonyl]amino]-5-carbamimidamidopentanoyl]amino]-4-carboxybutanoyl]amino]-5-carbamimidamidopentanoyl]amino]-3-hydroxypropanoyl]amino]-5-carbamimidamidopentanoyl]amino]-4-methylpentanoyl]amino]-4-methylpentanoic acid")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_56842206.jpg", caption=f"SMILES: CC[C@H](C)C(NC(=O)C(C)NC(=O)C(C)NC(=O)C(NC(=O)C(CC(C)C)NC(=O)C(N)CCSC)C(C)C)C(=O)NC(CCC(N)=O)C(=O)NC(CO)C(=O)NC(C)C(=O)NCC(=O)NC(CC(C)C)C(=O)NC(C(=O)NC(CCC(=O)O)C(=O)NC(C(=O)NC(CC(C)C)C(=O)NC(CC(N)=O)C(=O)NC(CCCN=C(N)N)C(=O)NC(CCC(=O)O)C(=O)NCC(=O)NC(C(=O)NC(Cc1ccc(O)cc1)C(=O)NC(C(=O)NC(C(=O)NC(Cc1ccccc1)C(=O)NC(C)C(=O)N1CCCC1C(=O)NC(C(=O)NC(CC(N)=O)C(=O)NC(CCC(=O)O)C(=O)NC(C)C(=O)NC(Cc1ccccc1)C(=O)NC(CCCNC(=N)N)C(=O)NC(C)C(=O)NC(CC(C)C)C(=O)N1CCCC1C(=O)N1CCCC1C(=O)NC(CCCNC(=N)N)C(=O)NC(CCC(=O)O)C(=O)NC(CCCNC(=N)N)C(=O)NC(CO)C(=O)NC(CCCNC(=N)N)C(=O)NC(CC(C)C)C(=O)NC(CC(C)C)C(=O)O)[C@@H](C)O)C(C)C)[C@@H](C)O)C(C)C)[C@@H](C)O)[C@@H](C)O")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 56842206) ]

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

    