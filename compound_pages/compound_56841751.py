
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Urogastrone", layout="wide")
st.title("Urogastrone")
st.markdown(f"PubChem Compound ID: [56841751](https://pubchem.ncbi.nlm.nih.gov/compound/56841751)")
st.markdown(f"IUPAC Name: (4S)-4-[[(2S)-2-[[(2S)-2-[[(2S)-2-[[(2S)-2-[[(2S)-2-[[(2S)-2-[[(2S,3R)-2-[[(2S)-5-amino-2-[[(2R)-2-[[(2S)-2-[[(2S)-2-[[2-[[(2S)-2-[[(2S)-2-[[2-[[(2S,3S)-2-[[(2S)-2-[[(2R)-2-[[(2S)-4-amino-2-[[(2R)-2-[[(2S,3R)-2-[[(2S)-2-[[(2S)-2-[[(2S)-2-[[(2S)-2-[[(2S)-2-[[(2S)-2-[[(2S,3S)-2-[[(2S)-2-[[(2S)-2-[[(2R)-2-[[(2S)-2-[[2-[[2-[[(2S)-4-amino-2-[[(2S)-2-[[(2R)-2-[[(2S)-2-[[2-[[(2S)-3-carboxy-2-[[(2S)-2-[[(2S)-2-[[(2S)-2-[[(2S)-1-[(2R)-2-[[2-[[(2S)-1-[(2S)-2-[[(2S)-2-[[(2S)-2,4-diamino-4-oxobutanoyl]amino]-3-hydroxypropanoyl]amino]-3-(4-hydroxyphenyl)propanoyl]pyrrolidine-2-carbonyl]amino]acetyl]amino]-3-sulfanylpropanoyl]pyrrolidine-2-carbonyl]amino]-3-hydroxypropanoyl]amino]-3-hydroxypropanoyl]amino]-3-(4-hydroxyphenyl)propanoyl]amino]propanoyl]amino]acetyl]amino]-3-(4-hydroxyphenyl)propanoyl]amino]-3-sulfanylpropanoyl]amino]-4-methylpentanoyl]amino]-4-oxobutanoyl]amino]acetyl]amino]acetyl]amino]-3-methylbutanoyl]amino]-3-sulfanylpropanoyl]amino]-4-methylsulfanylbutanoyl]amino]-3-(1H-imidazol-5-yl)propanoyl]amino]-3-methylpentanoyl]amino]-4-carboxybutanoyl]amino]-3-hydroxypropanoyl]amino]-4-methylpentanoyl]amino]-3-carboxypropanoyl]amino]-3-hydroxypropanoyl]amino]-3-(4-hydroxyphenyl)propanoyl]amino]-3-hydroxybutanoyl]amino]-3-sulfanylpropanoyl]amino]-4-oxobutanoyl]amino]-3-sulfanylpropanoyl]amino]-3-methylbutanoyl]amino]-3-methylpentanoyl]amino]acetyl]amino]-3-(4-hydroxyphenyl)propanoyl]amino]-3-hydroxypropanoyl]amino]acetyl]amino]-3-carboxypropanoyl]amino]-5-carbamimidamidopentanoyl]amino]-3-sulfanylpropanoyl]amino]-5-oxopentanoyl]amino]-3-hydroxybutanoyl]amino]-5-carbamimidamidopentanoyl]amino]-3-carboxypropanoyl]amino]-4-methylpentanoyl]amino]-5-carbamimidamidopentanoyl]amino]-3-(1H-indol-3-yl)propanoyl]amino]-3-(1H-indol-3-yl)propanoyl]amino]-5-[[(2S)-1-[[(1S)-4-carbamimidamido-1-carboxybutyl]amino]-4-methyl-1-oxopentan-2-yl]amino]-5-oxopentanoic acid")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_56841751.jpg", width=400)

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 56841751) ]

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

    