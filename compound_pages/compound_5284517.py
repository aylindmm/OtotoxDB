
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Astromicin", layout="wide")
st.title("Astromicin")
st.markdown(f"PubChem Compound ID: [5284517](https://pubchem.ncbi.nlm.nih.gov/compound/5284517)")
st.markdown(f"IUPAC Name: 2-amino-N-[(1S,2R,3R,4S,5S,6R)-4-amino-3-[(2R,3R,6S)-3-amino-6-[(1S)-1-aminoethyl]oxan-2-yl]oxy-2,5-dihydroxy-6-methoxycyclohexyl]-N-methylacetamide")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_5284517.jpg", caption=f"SMILES: CO[C@H]1[C@@H](O)[C@H](N)[C@@H](O[C@H]2O[C@H]([C@H](C)N)CC[C@H]2N)[C@H](O)[C@@H]1N(C)C(=O)CN")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 5284517) ]

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

    