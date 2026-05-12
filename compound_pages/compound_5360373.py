
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Bleomycin", layout="wide")
st.title("Bleomycin")
st.markdown(f"PubChem Compound ID: [5360373](https://pubchem.ncbi.nlm.nih.gov/compound/5360373)")
st.markdown(f"IUPAC Name: 3-[[2-[2-[2-[[(2S,3R)-2-[[(2S,3S,4R)-4-[[(2S,3R)-2-[[6-amino-2-[(1S)-3-amino-1-[[(2S)-2,3-diamino-3-oxopropyl]amino]-3-oxopropyl]-5-methylpyrimidine-4-carbonyl]amino]-3-[3-[4-carbamoyloxy-3,5-dihydroxy-6-(hydroxymethyl)oxan-2-yl]oxy-4,5-dihydroxy-6-(hydroxymethyl)oxan-2-yl]oxy-3-(1H-imidazol-5-yl)propanoyl]amino]-3-hydroxy-2-methylpentanoyl]amino]-3-hydroxybutanoyl]amino]ethyl]-1,3-thiazol-4-yl]-1,3-thiazole-4-carbonyl]amino]propyl-dimethylsulfanium")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_5360373.jpg", width=400)

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 5360373) ]

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

    