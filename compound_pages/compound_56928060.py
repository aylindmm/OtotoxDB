
import streamlit as st
import pandas as pd

st.set_page_config(page_title="GLYCOPEPTIDE", layout="wide")
st.title("GLYCOPEPTIDE")
st.markdown(f"PubChem Compound ID: [56928060](https://pubchem.ncbi.nlm.nih.gov/compound/56928060)")
st.markdown(f"IUPAC Name: (2S)-2-[[(2R)-2-[[(4R)-4-[[(2R)-2-[2-[(3R,4R,5S,6R)-5-[(2S,3R,4R,5S,6R)-3-acetamido-4,5-dihydroxy-6-(hydroxymethyl)oxan-2-yl]oxy-3-(ethylamino)-2-hydroxy-6-(hydroxymethyl)oxan-4-yl]oxypropanoylamino]propanoyl]amino]-5-amino-5-oxopentanoyl]amino]-6-aminohexanoyl]amino]propanoic acid")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_56928060.jpg", caption=f"SMILES: CCN[C@H]1C(O)O[C@H](CO)[C@@H](O[C@@H]2O[C@H](CO)[C@@H](O)[C@H](O)[C@H]2NC(C)=O)[C@@H]1OC(C)C(=O)NC(C)C(=O)NC(CCC(=O)NC(CCCCN)C(=O)NC(C)C(=O)O)C(N)=O")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 56928060) ]

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

    