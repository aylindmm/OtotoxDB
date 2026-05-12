
import streamlit as st
import pandas as pd

st.set_page_config(page_title="alpha-CYCLODEXTRIN", layout="wide")
st.title("alpha-CYCLODEXTRIN")
st.markdown(f"PubChem Compound ID: [444913](https://pubchem.ncbi.nlm.nih.gov/compound/444913)")
st.markdown(f"IUPAC Name: (1S,3R,5R,6S,8R,10R,11S,13R,15R,16S,18R,20R,21S,23R,25R,26S,28R,30R,31R,32R,33R,34R,35R,36R,37R,38R,39R,40R,41R,42R)-5,10,15,20,25,30-hexakis(hydroxymethyl)-2,4,7,9,12,14,17,19,22,24,27,29-dodecaoxaheptacyclo[26.2.2.23,6.28,11.213,16.218,21.223,26]dotetracontane-31,32,33,34,35,36,37,38,39,40,41,42-dodecol")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_444913.jpg", caption=f"SMILES: OC[C@H]1O[C@@H]2O[C@H]3[C@H](O)[C@@H](O)[C@@H](O[C@H]4[C@H](O)[C@@H](O)[C@@H](O[C@H]5[C@H](O)[C@@H](O)[C@@H](O[C@H]6[C@H](O)[C@@H](O)[C@@H](O[C@H]7[C@H](O)[C@@H](O)[C@@H](O[C@H]1[C@H](O)[C@H]2O)O[C@@H]7CO)O[C@@H]6CO)O[C@@H]5CO)O[C@@H]4CO)O[C@@H]3CO")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 444913) ]

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

    