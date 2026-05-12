
import streamlit as st
import pandas as pd

st.set_page_config(page_title="erythromycin", layout="wide")
st.title("erythromycin")
st.markdown(f"PubChem Compound ID: [12560](https://pubchem.ncbi.nlm.nih.gov/compound/12560)")
st.markdown(f"IUPAC Name: (3R,4S,5S,6R,7R,9R,11R,12R,13S,14R)-6-[(2S,3R,4S,6R)-4-(dimethylamino)-3-hydroxy-6-methyloxan-2-yl]oxy-14-ethyl-7,12,13-trihydroxy-4-[(2R,4R,5S,6S)-5-hydroxy-4-methoxy-4,6-dimethyloxan-2-yl]oxy-3,5,7,9,11,13-hexamethyl-oxacyclotetradecane-2,10-dione")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_12560.jpg", caption=f"SMILES: CC[C@H]1OC(=O)C(C)[C@@H](O[C@H]2C[C@@](C)(OC)[C@@H](O)[C@H](C)O2)[C@H](C)[C@@H](O[C@@H]2O[C@H](C)C[C@H](N(C)C)[C@H]2O)[C@](C)(O)CC(C)C(=O)C(C)[C@@H](O)[C@]1(C)O")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 12560) ]

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

    