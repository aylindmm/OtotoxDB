
import streamlit as st
import pandas as pd

st.set_page_config(page_title="bromocriptine", layout="wide")
st.title("bromocriptine")
st.markdown(f"PubChem Compound ID: [31101](https://pubchem.ncbi.nlm.nih.gov/compound/31101)")
st.markdown(f"IUPAC Name: (6aR,9R)-5-bromo-N-[(1S,2S,4R,7S)-2-hydroxy-7-(2-methylpropyl)-5,8-dioxo-4-propan-2-yl-3-oxa-6,9-diazatricyclo[7.3.0.02,6]dodecan-4-yl]-7-methyl-6,6a,8,9-tetrahydro-4H-indolo[4,3-fg]quinoline-9-carboxamide")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_31101.jpg", caption=f"SMILES: CC(C)CC1C(=O)N2CCC[C@H]2[C@]2(O)O[C@](NC(=O)C3C=C4c5cccc6[nH]c(Br)c(c56)C[C@H]4N(C)C3)(C(C)C)C(=O)N12")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 31101) ]

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

    