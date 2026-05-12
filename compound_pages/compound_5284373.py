
import streamlit as st
import pandas as pd

st.set_page_config(page_title="cyclosporin A", layout="wide")
st.title("cyclosporin A")
st.markdown(f"PubChem Compound ID: [5284373](https://pubchem.ncbi.nlm.nih.gov/compound/5284373)")
st.markdown(f"IUPAC Name: (3S,6S,9S,12R,15S,18S,21S,24S,30S,33S)-30-ethyl-33-[(E,1R,2R)-1-hydroxy-2-methylhex-4-enyl]-1,4,7,10,12,15,19,25,28-nonamethyl-6,9,18,24-tetrakis(2-methylpropyl)-3,21-di(propan-2-yl)-1,4,7,10,13,16,19,22,25,28,31-undecazacyclotritriacontane-2,5,8,11,14,17,20,23,26,29,32-undecone")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_5284373.jpg", caption=f"SMILES: C/C=C/C[C@@H](C)[C@@H](O)C1C(=O)NC(CC)C(=O)N(C)CC(=O)N(C)C(CC(C)C)C(=O)NC(C(C)C)C(=O)N(C)C(CC(C)C)C(=O)NC(C)C(=O)NC(C)C(=O)N(C)C(CC(C)C)C(=O)N(C)C(CC(C)C)C(=O)N(C)C(C(C)C)C(=O)N1C")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 5284373) ]

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

    