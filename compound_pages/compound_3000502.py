
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Capostatin", layout="wide")
st.title("Capostatin")
st.markdown(f"PubChem Compound ID: [3000502](https://pubchem.ncbi.nlm.nih.gov/compound/3000502)")
st.markdown(f"IUPAC Name: (3S)-3,6-diamino-N-[[(2S,5S,8E,11S,15S)-15-amino-11-[(6R)-2-amino-1,4,5,6-tetrahydropyrimidin-6-yl]-8-[(carbamoylamino)methylidene]-2-(hydroxymethyl)-3,6,9,12,16-pentaoxo-1,4,7,10,13-pentazacyclohexadec-5-yl]methyl]hexanamide;(3S)-3,6-diamino-N-[[(2S,5S,8E,11S,15S)-15-amino-11-[(6R)-2-amino-1,4,5,6-tetrahydropyrimidin-6-yl]-8-[(carbamoylamino)methylidene]-2-methyl-3,6,9,12,16-pentaoxo-1,4,7,10,13-pentazacyclohexadec-5-yl]methyl]hexanamide")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_3000502.jpg", caption=f"SMILES: CC1NC(=O)C(N)CNC(=O)C([C@H]2CCN=C(N)N2)NC(=O)C(=CNC(N)=O)NC(=O)C(CNC(=O)C[C@@H](N)CCCN)NC1=O.NCCC[C@H](N)CC(=O)NCC1NC(=O)C(CO)NC(=O)C(N)CNC(=O)C([C@H]2CCN=C(N)N2)NC(=O)C(=CNC(N)=O)NC1=O")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 3000502) ]

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

    