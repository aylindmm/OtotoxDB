
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Peptide PACAP", layout="wide")
st.title("Peptide PACAP")
st.markdown(f"PubChem Compound ID: [133082079](https://pubchem.ncbi.nlm.nih.gov/compound/133082079)")
st.markdown(f"IUPAC Name: (3S)-4-[[2-[[(2S,3S)-1-[[(2S)-1-[[(2S,3R)-1-[[(2S)-1-[[(2S)-1-[[(2S)-1-[[(2S)-1-[[(2S)-1-[[(2S)-1-[[(2S)-1-[[(2S)-6-amino-1-[[(2S)-5-amino-1-[[(2S)-1-[[(2S)-1-[[(2S)-1-[[(2S)-6-amino-1-[[(2S)-6-amino-1-[[(2S)-1-[[(2S)-1-[[(2S)-1-[[(2S)-1-[[(2S)-1-[[(2S)-1-[[2-[[(2S)-6-amino-1-[[2-[[(2S)-1-[[(2S)-6-amino-1-[[(2S)-5-amino-1-[[(2S)-1-[[(2S)-1-[[(2S)-6-amino-1-[[(2S)-4-amino-1-[[(2S)-1,6-diamino-1-oxohexan-2-yl]amino]-1,4-dioxobutan-2-yl]amino]-1-oxohexan-2-yl]amino]-3-methyl-1-oxobutan-2-yl]amino]-5-carbamimidamido-1-oxopentan-2-yl]amino]-1,5-dioxopentan-2-yl]amino]-1-oxohexan-2-yl]amino]-3-(4-hydroxyphenyl)-1-oxopropan-2-yl]amino]-2-oxoethyl]amino]-1-oxohexan-2-yl]amino]-2-oxoethyl]amino]-4-methyl-1-oxopentan-2-yl]amino]-3-methyl-1-oxobutan-2-yl]amino]-1-oxopropan-2-yl]amino]-1-oxopropan-2-yl]amino]-4-methyl-1-oxopentan-2-yl]amino]-3-(4-hydroxyphenyl)-1-oxopropan-2-yl]amino]-1-oxohexan-2-yl]amino]-1-oxohexan-2-yl]amino]-3-methyl-1-oxobutan-2-yl]amino]-1-oxopropan-2-yl]amino]-4-methylsulfanyl-1-oxobutan-2-yl]amino]-1,5-dioxopentan-2-yl]amino]-1-oxohexan-2-yl]amino]-5-carbamimidamido-1-oxopentan-2-yl]amino]-3-(4-hydroxyphenyl)-1-oxopropan-2-yl]amino]-5-carbamimidamido-1-oxopentan-2-yl]amino]-3-hydroxy-1-oxopropan-2-yl]amino]-3-(4-hydroxyphenyl)-1-oxopropan-2-yl]amino]-3-hydroxy-1-oxopropan-2-yl]amino]-3-carboxy-1-oxopropan-2-yl]amino]-3-hydroxy-1-oxobutan-2-yl]amino]-1-oxo-3-phenylpropan-2-yl]amino]-3-methyl-1-oxopentan-2-yl]amino]-2-oxoethyl]amino]-3-[[(2S)-2-[[(2S)-2-amino-3-(1H-imidazol-5-yl)propanoyl]amino]-3-hydroxypropanoyl]amino]-4-oxobutanoic acid")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_133082079.jpg", caption=f"SMILES: CC[C@H](C)C(NC(=O)CNC(=O)C(CC(=O)O)NC(=O)C(CO)NC(=O)C(N)Cc1c[nH]cn1)C(=O)NC(Cc1ccccc1)C(=O)NC(C(=O)NC(CC(=O)O)C(=O)NC(CO)C(=O)NC(Cc1ccc(O)cc1)C(=O)NC(CO)C(=O)NC(CCCNC(=N)N)C(=O)NC(Cc1ccc(O)cc1)C(=O)NC(CCCNC(=N)N)C(=O)NC(CCCCN)C(=O)NC(CCC(N)=O)C(=O)NC(CCSC)C(=O)NC(C)C(=O)NC(C(=O)NC(CCCCN)C(=O)NC(CCCCN)C(=O)NC(Cc1ccc(O)cc1)C(=O)NC(CC(C)C)C(=O)NC(C)C(=O)NC(C)C(=O)NC(C(=O)NC(CC(C)C)C(=O)NCC(=O)NC(CCCCN)C(=O)NCC(=O)NC(Cc1ccc(O)cc1)C(=O)NC(CCCCN)C(=O)NC(CCC(N)=O)C(=O)NC(CCCNC(=N)N)C(=O)NC(C(=O)NC(CCCCN)C(=O)NC(CC(N)=O)C(=O)NC(CCCCN)C(N)=O)C(C)C)C(C)C)C(C)C)[C@@H](C)O")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 133082079) ]

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

    