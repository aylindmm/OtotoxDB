
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Colistin", layout="wide")
st.title("Colistin")
st.markdown(f"PubChem Compound ID: [5311054](https://pubchem.ncbi.nlm.nih.gov/compound/5311054)")
st.markdown(f"IUPAC Name: N-[(2S)-4-amino-1-[[(2S,3R)-1-[[(2S)-4-amino-1-oxo-1-[[(3S,6S,9S,12S,15R,18S,21S)-6,9,18-tris(2-aminoethyl)-3-[(1R)-1-hydroxyethyl]-12,15-bis(2-methylpropyl)-2,5,8,11,14,17,20-heptaoxo-1,4,7,10,13,16,19-heptazacyclotricos-21-yl]amino]butan-2-yl]amino]-3-hydroxy-1-oxobutan-2-yl]amino]-1-oxobutan-2-yl]-5-methylheptanamide")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_5311054.jpg", width=400)

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 5311054) ]

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

    