
import streamlit as st
import pandas as pd

st.set_page_config(page_title="TAPI-1", layout="wide")
st.title("TAPI-1")
st.markdown(f"PubChem Compound ID: [10458621](https://pubchem.ncbi.nlm.nih.gov/compound/10458621)")
st.markdown(f"IUPAC Name: (2R)-N-[(2S)-1-[[(2S)-1-(2-aminoethylamino)-1-oxopropan-2-yl]amino]-3-naphthalen-2-yl-1-oxopropan-2-yl]-N'-hydroxy-2-(2-methylpropyl)butanediamide")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_10458621.jpg", caption=f"SMILES: CC(C)CC(CC(O)=NO)C(=O)NC(Cc1ccc2ccccc2c1)C(=O)NC(C)C(=O)NCCN")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 10458621) ]

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

    