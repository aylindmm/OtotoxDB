
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Lixisenatide", layout="wide")
st.title("Lixisenatide")
st.markdown(f"PubChem Compound ID: [90472060](https://pubchem.ncbi.nlm.nih.gov/compound/90472060)")
st.markdown(f"IUPAC Name: (4S)-5-[[2-[[(2S,3R)-1-[[(2S)-1-[[(2S,3R)-1-[[(2S)-1-[[(2S)-1-[[(2S)-1-[[(2S)-1-[[(2S)-6-amino-1-[[(2S)-5-amino-1-[[(2S)-1-[[(2S)-1-[[(2S)-1-[[(2S)-1-[[(2S)-1-[[(2S)-1-[[(2S)-1-[[(2S)-1-[[(2S)-1-[[(2S,3S)-1-[[(2S)-1-[[(2S)-1-[[(2S)-1-[[(2S)-6-amino-1-[[(2S)-4-amino-1-[[2-[[2-[(2S)-2-[[(2S)-1-[[(2S)-1-[[2-[[(2S)-1-[(2S)-2-[(2S)-2-[[(2S)-1-[[(2S)-6-amino-1-[[(2S)-6-amino-1-[[(2S)-6-amino-1-[[(2S)-6-amino-1-[[(2S)-6-amino-1-[[(2S)-1,6-diamino-1-oxohexan-2-yl]amino]-1-oxohexan-2-yl]amino]-1-oxohexan-2-yl]amino]-1-oxohexan-2-yl]amino]-1-oxohexan-2-yl]amino]-1-oxohexan-2-yl]amino]-3-hydroxy-1-oxopropan-2-yl]carbamoyl]pyrrolidine-1-carbonyl]pyrrolidin-1-yl]-1-oxopropan-2-yl]amino]-2-oxoethyl]amino]-3-hydroxy-1-oxopropan-2-yl]amino]-3-hydroxy-1-oxopropan-2-yl]carbamoyl]pyrrolidin-1-yl]-2-oxoethyl]amino]-2-oxoethyl]amino]-1,4-dioxobutan-2-yl]amino]-1-oxohexan-2-yl]amino]-4-methyl-1-oxopentan-2-yl]amino]-3-(1H-indol-3-yl)-1-oxopropan-2-yl]amino]-4-carboxy-1-oxobutan-2-yl]amino]-3-methyl-1-oxopentan-2-yl]amino]-1-oxo-3-phenylpropan-2-yl]amino]-4-methyl-1-oxopentan-2-yl]amino]-5-carbamimidamido-1-oxopentan-2-yl]amino]-3-methyl-1-oxobutan-2-yl]amino]-1-oxopropan-2-yl]amino]-4-carboxy-1-oxobutan-2-yl]amino]-4-carboxy-1-oxobutan-2-yl]amino]-4-carboxy-1-oxobutan-2-yl]amino]-4-methylsulfanyl-1-oxobutan-2-yl]amino]-1,5-dioxopentan-2-yl]amino]-1-oxohexan-2-yl]amino]-3-hydroxy-1-oxopropan-2-yl]amino]-4-methyl-1-oxopentan-2-yl]amino]-3-carboxy-1-oxopropan-2-yl]amino]-3-hydroxy-1-oxopropan-2-yl]amino]-3-hydroxy-1-oxobutan-2-yl]amino]-1-oxo-3-phenylpropan-2-yl]amino]-3-hydroxy-1-oxobutan-2-yl]amino]-2-oxoethyl]amino]-4-[[2-[[(2S)-2-amino-3-(1H-imidazol-4-yl)propanoyl]amino]acetyl]amino]-5-oxopentanoic acid")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_90472060.jpg", caption=f"SMILES: CC[C@H](C)C(NC(=O)C(Cc1ccccc1)NC(=O)C(CC(C)C)NC(=O)C(CCCN=C(N)N)NC(=O)C(NC(=O)C(C)NC(=O)C(CCC(=O)O)NC(=O)C(CCC(=O)O)NC(=O)C(CCC(=O)O)NC(=O)C(CCSC)NC(=O)C(CCC(N)=O)NC(=O)C(CCCCN)NC(=O)C(CO)NC(=O)C(CC(C)C)NC(=O)C(CC(=O)O)NC(=O)C(CO)NC(=O)C(NC(=O)C(Cc1ccccc1)NC(=O)C(NC(=O)CNC(=O)C(CCC(=O)O)NC(=O)CNC(=O)C(N)Cc1c[nH]cn1)[C@@H](C)O)[C@@H](C)O)C(C)C)C(=O)NC(CCC(=O)O)C(=O)NC(Cc1c[nH]c2ccccc12)C(=O)NC(CC(C)C)C(=O)NC(CCCCN)C(=O)NC(CC(N)=O)C(=O)NCC(=O)NCC(=O)N1CCCC1C(=O)NC(CO)C(=O)NC(CO)C(=O)NCC(=O)NC(C)C(=O)N1CCCC1C(=O)N1CCCC1C(=O)NC(CO)C(=O)NC(CCCCN)C(=O)NC(CCCCN)C(=O)NC(CCCCN)C(=O)NC(CCCCN)C(=O)NC(CCCCN)C(=O)NC(CCCCN)C(N)=O")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 90472060) ]

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

    