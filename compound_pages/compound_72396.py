
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Gentamicin C1a", layout="wide")
st.title("Gentamicin C1a")
st.markdown(f"PubChem Compound ID: [72396](https://pubchem.ncbi.nlm.nih.gov/compound/72396)")
st.markdown(f"IUPAC Name: (2R,3R,4R,5R)-2-[(1S,2S,3R,4S,6R)-4,6-diamino-3-[(2R,3R,6S)-3-amino-6-(aminomethyl)oxan-2-yl]oxy-2-hydroxycyclohexyl]oxy-5-methyl-4-(methylamino)oxane-3,5-diol")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_72396.jpg", caption=f"SMILES: CN[C@@H]1[C@@H](O)[C@@H](O[C@@H]2[C@@H](O)[C@H](O[C@H]3O[C@H](CN)CC[C@H]3N)[C@@H](N)C[C@H]2N)OC[C@]1(C)O")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 72396) ]

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

    