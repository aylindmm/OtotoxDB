
import streamlit as st
import pandas as pd

st.set_page_config(page_title="213546-53-3", layout="wide")
st.title("213546-53-3")
st.markdown(f"PubChem Compound ID: [16209942](https://pubchem.ncbi.nlm.nih.gov/compound/16209942)")
st.markdown(f"IUPAC Name: (2S)-1-[(2S)-2-[[(2S)-2-[[(2S)-6-amino-2-[[(2S)-5-amino-2-[[(2S)-2-[[(2S)-6-amino-2-[[(2S)-2-[[(2S)-5-amino-2-[[(2S)-2-[[(2S)-1-[(2S)-2-[[(2S)-2-[[(2S)-2-[[(2S)-2-[[(2S)-2-[[(2S)-2-[[(2S)-2-[[(2S)-2-[[(2S)-1-[(2S)-2-[[(2S)-2-[[(2S)-2-[[(2S)-2-[[(2S)-2-[[(2S)-2-aminopropanoyl]amino]propanoyl]amino]-3-methylbutanoyl]amino]propanoyl]amino]-4-methylpentanoyl]amino]-4-methylpentanoyl]pyrrolidine-2-carbonyl]amino]propanoyl]amino]-3-methylbutanoyl]amino]-4-methylpentanoyl]amino]-4-methylpentanoyl]amino]propanoyl]amino]-4-methylpentanoyl]amino]-4-methylpentanoyl]amino]propanoyl]pyrrolidine-2-carbonyl]amino]-3-methylbutanoyl]amino]-5-oxopentanoyl]amino]-5-carbamimidamidopentanoyl]amino]hexanoyl]amino]-5-carbamimidamidopentanoyl]amino]-5-oxopentanoyl]amino]hexanoyl]amino]-4-methylpentanoyl]amino]-4-methylsulfanylbutanoyl]pyrrolidine-2-carboxylic acid")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_16209942.jpg", width=400)

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 16209942) ]

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

    