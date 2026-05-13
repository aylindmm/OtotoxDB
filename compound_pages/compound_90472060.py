
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Lixisenatide", layout="wide")
st.title("Lixisenatide")
# Display the image in Streamlit
st.image(f"compound_structures/compound_90472060.jpg", width=300)
st.markdown(f"PubChem Compound ID: [90472060](https://pubchem.ncbi.nlm.nih.gov/compound/90472060)")
st.markdown(f"IUPAC Name: (4S)-5-[[2-[[(2S,3R)-1-[[(2S)-1-[[(2S,3R)-1-[[(2S)-1-[[(2S)-1-[[(2S)-1-[[(2S)-1-[[(2S)-6-amino-1-[[(2S)-5-amino-1-[[(2S)-1-[[(2S)-1-[[(2S)-1-[[(2S)-1-[[(2S)-1-[[(2S)-1-[[(2S)-1-[[(2S)-1-[[(2S)-1-[[(2S,3S)-1-[[(2S)-1-[[(2S)-1-[[(2S)-1-[[(2S)-6-amino-1-[[(2S)-4-amino-1-[[2-[[2-[(2S)-2-[[(2S)-1-[[(2S)-1-[[2-[[(2S)-1-[(2S)-2-[(2S)-2-[[(2S)-1-[[(2S)-6-amino-1-[[(2S)-6-amino-1-[[(2S)-6-amino-1-[[(2S)-6-amino-1-[[(2S)-6-amino-1-[[(2S)-1,6-diamino-1-oxohexan-2-yl]amino]-1-oxohexan-2-yl]amino]-1-oxohexan-2-yl]amino]-1-oxohexan-2-yl]amino]-1-oxohexan-2-yl]amino]-1-oxohexan-2-yl]amino]-3-hydroxy-1-oxopropan-2-yl]carbamoyl]pyrrolidine-1-carbonyl]pyrrolidin-1-yl]-1-oxopropan-2-yl]amino]-2-oxoethyl]amino]-3-hydroxy-1-oxopropan-2-yl]amino]-3-hydroxy-1-oxopropan-2-yl]carbamoyl]pyrrolidin-1-yl]-2-oxoethyl]amino]-2-oxoethyl]amino]-1,4-dioxobutan-2-yl]amino]-1-oxohexan-2-yl]amino]-4-methyl-1-oxopentan-2-yl]amino]-3-(1H-indol-3-yl)-1-oxopropan-2-yl]amino]-4-carboxy-1-oxobutan-2-yl]amino]-3-methyl-1-oxopentan-2-yl]amino]-1-oxo-3-phenylpropan-2-yl]amino]-4-methyl-1-oxopentan-2-yl]amino]-5-carbamimidamido-1-oxopentan-2-yl]amino]-3-methyl-1-oxobutan-2-yl]amino]-1-oxopropan-2-yl]amino]-4-carboxy-1-oxobutan-2-yl]amino]-4-carboxy-1-oxobutan-2-yl]amino]-4-carboxy-1-oxobutan-2-yl]amino]-4-methylsulfanyl-1-oxobutan-2-yl]amino]-1,5-dioxopentan-2-yl]amino]-1-oxohexan-2-yl]amino]-3-hydroxy-1-oxopropan-2-yl]amino]-4-methyl-1-oxopentan-2-yl]amino]-3-carboxy-1-oxopropan-2-yl]amino]-3-hydroxy-1-oxopropan-2-yl]amino]-3-hydroxy-1-oxobutan-2-yl]amino]-1-oxo-3-phenylpropan-2-yl]amino]-3-hydroxy-1-oxobutan-2-yl]amino]-2-oxoethyl]amino]-4-[[2-[[(2S)-2-amino-3-(1H-imidazol-4-yl)propanoyl]amino]acetyl]amino]-5-oxopentanoic acid")
st.markdown(f"Score: 0.0134498991257566")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 90472060) ]


df_filtered['PMID'] = df_filtered['PMID'].apply(lambda x: f"https://pubmed.ncbi.nlm.nih.gov/{x}/")  

variable_labels = {
    "ototoxic_drugs": "Ototoxic Reports",
    "otoprotective_drugs": "Otoprotective Reports",
}


for variable in df_filtered['variable'].unique():

    label = variable_labels.get(variable, variable)  # falls back to raw name if not in dict
    st.markdown(f"**{label}**")
    source_df = df_filtered[df_filtered['variable'] == variable]
    st.dataframe(
        source_df[["PMID", "Title", "Year"]].rename(columns={"PMID": "PubMed ID", "Title": "Title", "Year": "Year"}),
        use_container_width=True,
        column_config={
            "PubMed ID": st.column_config.LinkColumn("PubMed ID", display_text="https://pubmed.ncbi.nlm.nih.gov/(.*?)/"),
            "Title": st.column_config.TextColumn("Title"),
        },
        hide_index=True,
    )


if st.button("Back"):
    st.switch_page("pages/1_Home.py")

    