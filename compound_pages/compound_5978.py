
import streamlit as st
import pandas as pd

st.set_page_config(page_title="vincristine", layout="wide")
st.title("vincristine")
st.markdown(f"PubChem Compound ID: [5978](https://pubchem.ncbi.nlm.nih.gov/compound/5978)")
st.markdown(f"IUPAC Name: methyl (1R,9R,10S,11R,12R,19R)-11-acetyloxy-12-ethyl-4-[(13S,15S,17S)-17-ethyl-17-hydroxy-13-methoxycarbonyl-1,11-diazatetracyclo[13.3.1.04,12.05,10]nonadeca-4(12),5,7,9-tetraen-13-yl]-8-formyl-10-hydroxy-5-methoxy-8,16-diazapentacyclo[10.6.1.01,9.02,7.016,19]nonadeca-2,4,6,13-tetraene-10-carboxylate")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_5978.jpg", caption=f"SMILES: CC[C@]1(O)C[C@H]2CN(CCc3c([nH]c4ccccc34)[C@@](C(=O)OC)(c3cc4c(cc3OC)N(C=O)[C@H]3[C@@](O)(C(=O)OC)[C@H](OC(C)=O)[C@]5(CC)C=CCN6CC[C@]43[C@@H]65)C2)C1")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 5978) ]

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

    