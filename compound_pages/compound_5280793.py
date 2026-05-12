
import streamlit as st
import pandas as pd

st.set_page_config(page_title="ergocalciferol", layout="wide")
st.title("ergocalciferol")
st.markdown(f"PubChem Compound ID: [5280793](https://pubchem.ncbi.nlm.nih.gov/compound/5280793)")
st.markdown(f"IUPAC Name: (1S,3Z)-3-[(2E)-2-[(1R,3aS,7aR)-1-[(E,2R,5R)-5,6-dimethylhept-3-en-2-yl]-7a-methyl-2,3,3a,5,6,7-hexahydro-1H-inden-4-ylidene]ethylidene]-4-methylidenecyclohexan-1-ol")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_5280793.jpg", caption=f"SMILES: C=C1CC[C@H](O)C/C1=C/C=C1CCC[C@]2(C)[C@@H]([C@H](C)/C=C/[C@H](C)C(C)C)CC[C@@H]12")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 5280793) ]

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

    