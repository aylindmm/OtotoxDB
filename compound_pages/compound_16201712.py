
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Gp91 ds-tat", layout="wide")
st.title("Gp91 ds-tat")
# Display the image in Streamlit
st.image(f"compound_structures/compound_16201712.jpg", width=300)
st.markdown(f"PubChem Compound ID: [16201712](https://pubchem.ncbi.nlm.nih.gov/compound/16201712)")
st.markdown(f"IUPAC Name: (2S)-2-[[(2S)-2-[[(2S)-2-[[(2S)-6-amino-2-[[(2S)-6-amino-2-[[(2S)-2-amino-5-carbamimidamidopentanoyl]amino]hexanoyl]amino]hexanoyl]amino]-5-carbamimidamidopentanoyl]amino]-5-carbamimidamidopentanoyl]amino]-N-[(2S)-1-[[(2S)-1-[[(2S)-1-[[(2R)-1-[[(2S)-1-[[(2S,3R)-1-[[(2S)-1-[[(2S,3S)-1-[[(2S)-1-[[(2S)-1-[[(2S)-5-amino-1-[[(2S)-1-amino-4-methyl-1-oxopentan-2-yl]amino]-1,5-dioxopentan-2-yl]amino]-5-carbamimidamido-1-oxopentan-2-yl]amino]-5-carbamimidamido-1-oxopentan-2-yl]amino]-3-methyl-1-oxopentan-2-yl]amino]-5-carbamimidamido-1-oxopentan-2-yl]amino]-3-hydroxy-1-oxobutan-2-yl]amino]-3-hydroxy-1-oxopropan-2-yl]amino]-1-oxo-3-sulfanylpropan-2-yl]amino]-5-carbamimidamido-1-oxopentan-2-yl]amino]-5-carbamimidamido-1-oxopentan-2-yl]amino]-5-carbamimidamido-1-oxopentan-2-yl]pentanediamide")
st.markdown(f"Score: -0.0134498991257566")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 16201712) ]

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

    