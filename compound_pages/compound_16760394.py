
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Z-DEVD-FMK", layout="wide")
st.title("Z-DEVD-FMK")
st.markdown(f"PubChem Compound ID: [16760394](https://pubchem.ncbi.nlm.nih.gov/compound/16760394)")
st.markdown(f"IUPAC Name: methyl (4S)-5-[[(2S)-1-[[(3S)-5-fluoro-1-methoxy-1,4-dioxopentan-3-yl]amino]-3-methyl-1-oxobutan-2-yl]amino]-4-[[(2S)-4-methoxy-4-oxo-2-(phenylmethoxycarbonylamino)butanoyl]amino]-5-oxopentanoate")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_16760394.jpg", caption=f"SMILES: COC(=O)CCC(NC(=O)C(CC(=O)OC)NC(=O)OCc1ccccc1)C(=O)NC(C(=O)NC(CC(=O)OC)C(=O)CF)C(C)C")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 16760394) ]

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

    