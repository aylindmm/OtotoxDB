
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Salmon calcitonin", layout="wide")
st.title("Salmon calcitonin")
# Display the image in Streamlit
st.image(f"compound_structures/compound_16220016.jpg", width=300)
st.markdown(f"PubChem Compound ID: [16220016](https://pubchem.ncbi.nlm.nih.gov/compound/16220016)")
st.markdown(f"IUPAC Name: (4S)-4-[[(2S)-5-amino-2-[[(2S)-2-[[(2S)-2-[[(2S)-6-amino-2-[[2-[[(2S)-2-[[(2S)-2-[[(4R,7S,10S,13S,16S,19S,22R)-22-amino-16-(2-amino-2-oxoethyl)-7-[(1R)-1-hydroxyethyl]-10,19-bis(hydroxymethyl)-13-(2-methylpropyl)-6,9,12,15,18,21-hexaoxo-1,2-dithia-5,8,11,14,17,20-hexazacyclotricosane-4-carbonyl]amino]-3-methylbutanoyl]amino]-4-methylpentanoyl]amino]acetyl]amino]hexanoyl]amino]-4-methylpentanoyl]amino]-3-hydroxypropanoyl]amino]-5-oxopentanoyl]amino]-5-[[(2S)-1-[[(2S)-1-[[(2S)-6-amino-1-[[(2S)-1-[[(2S)-5-amino-1-[[(2S,3R)-1-[[(2S)-1-[(2S)-2-[[(2S)-1-[[(2S,3R)-1-[[(2S)-4-amino-1-[[(2S,3R)-1-[[2-[[(2S)-1-[[2-[[(2S,3R)-1-[(2S)-2-carbamoylpyrrolidin-1-yl]-3-hydroxy-1-oxobutan-2-yl]amino]-2-oxoethyl]amino]-3-hydroxy-1-oxopropan-2-yl]amino]-2-oxoethyl]amino]-3-hydroxy-1-oxobutan-2-yl]amino]-1,4-dioxobutan-2-yl]amino]-3-hydroxy-1-oxobutan-2-yl]amino]-5-carbamimidamido-1-oxopentan-2-yl]carbamoyl]pyrrolidin-1-yl]-3-(4-hydroxyphenyl)-1-oxopropan-2-yl]amino]-3-hydroxy-1-oxobutan-2-yl]amino]-1,5-dioxopentan-2-yl]amino]-4-methyl-1-oxopentan-2-yl]amino]-1-oxohexan-2-yl]amino]-3-(1H-imidazol-5-yl)-1-oxopropan-2-yl]amino]-4-methyl-1-oxopentan-2-yl]amino]-5-oxopentanoic acid")
st.markdown(f"Score: -0.0134498991257566")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 16220016) ]

# Convert dataframe to CSV
csv = df_filtered.to_csv(index=False, sep='\t').encode('utf-8')

st.download_button(
    label="Download data as TSV",
    data=csv,
    file_name='articles.tsv',
    mime='text/tsv',
)


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

    