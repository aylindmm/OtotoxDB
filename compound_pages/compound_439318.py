
import streamlit as st
import pandas as pd

st.set_page_config(page_title="bekanamycin", layout="wide")
st.title("bekanamycin")
st.markdown(f"PubChem Compound ID: [439318](https://pubchem.ncbi.nlm.nih.gov/compound/439318)")
st.markdown(f"IUPAC Name: (2R,3S,4R,5R,6R)-5-amino-2-(aminomethyl)-6-[(1R,2S,3S,4R,6S)-4,6-diamino-3-[(2S,3R,4S,5S,6R)-4-amino-3,5-dihydroxy-6-(hydroxymethyl)oxan-2-yl]oxy-2-hydroxycyclohexyl]oxyoxane-3,4-diol")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_439318.jpg", caption=f"SMILES: NC[C@H]1O[C@H](O[C@H]2[C@H](O)[C@@H](O[C@H]3O[C@H](CO)[C@@H](O)[C@H](N)[C@H]3O)[C@H](N)C[C@@H]2N)[C@H](N)[C@@H](O)[C@@H]1O")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 439318) ]

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

    