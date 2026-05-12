
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Arbekacin", layout="wide")
st.title("Arbekacin")
st.markdown(f"PubChem Compound ID: [68682](https://pubchem.ncbi.nlm.nih.gov/compound/68682)")
st.markdown(f"IUPAC Name: (2S)-4-amino-N-[(1R,2S,3S,4R,5S)-5-amino-4-[(2R,3R,6S)-3-amino-6-(aminomethyl)oxan-2-yl]oxy-2-[(2S,3R,4S,5S,6R)-4-amino-3,5-dihydroxy-6-(hydroxymethyl)oxan-2-yl]oxy-3-hydroxycyclohexyl]-2-hydroxybutanamide")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_68682.jpg", caption=f"SMILES: NCCC(O)C(=O)N[C@@H]1C[C@H](N)[C@@H](O[C@H]2O[C@H](CN)CC[C@H]2N)[C@H](O)[C@H]1O[C@H]1O[C@H](CO)[C@@H](O)[C@H](N)[C@H]1O")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 68682) ]

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

    