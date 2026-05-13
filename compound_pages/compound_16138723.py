
import streamlit as st
import pandas as pd

st.set_page_config(page_title="151988-33-9", layout="wide")
st.title("151988-33-9")
# Display the image in Streamlit
st.image(f"compound_structures/compound_16138723.jpg", width=300)
st.markdown(f"PubChem Compound ID: [16138723](https://pubchem.ncbi.nlm.nih.gov/compound/16138723)")
st.markdown(f"IUPAC Name: (2S)-2-[[(2S)-2-[[(2S,3R)-2-[[(2S)-2-[[(2S)-2-[[(2S)-2-[[(2S)-2-[[(2S)-2-[[(2S)-2-[[(2S)-2-[[(2S)-2-[[(2S)-2-[[(2S,3S)-2-[[(2S)-2-[[(2S)-2-[[(2S)-2-[[(2S)-2-[[(2S)-2-[[(2S)-2-[[(2S)-2-[[(2S)-2-[[(2S)-2-[[(2S)-2-[[(2S)-2-[[(2S)-2-acetamidopropanoyl]amino]-4-methylsulfanylbutanoyl]amino]-3-methylbutanoyl]amino]-3-hydroxypropanoyl]amino]-4-carboxybutanoyl]amino]-3-phenylpropanoyl]amino]-4-methylpentanoyl]amino]-6-aminohexanoyl]amino]-5-amino-5-oxopentanoyl]amino]propanoyl]amino]-3-(1H-indol-3-yl)propanoyl]amino]-3-phenylpropanoyl]amino]-3-methylpentanoyl]amino]-4-carboxybutanoyl]amino]-4-amino-4-oxobutanoyl]amino]-4-carboxybutanoyl]amino]-4-carboxybutanoyl]amino]-5-amino-5-oxopentanoyl]amino]-4-carboxybutanoyl]amino]-3-(4-hydroxyphenyl)propanoyl]amino]-3-methylbutanoyl]amino]-5-amino-5-oxopentanoyl]amino]-3-hydroxybutanoyl]amino]-3-methylbutanoyl]amino]-6-aminohexanoic acid")
st.markdown(f"Score: -0.0134498991257566")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 16138723) ]

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

    