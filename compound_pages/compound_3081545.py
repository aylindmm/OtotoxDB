
import streamlit as st
import pandas as pd

st.set_page_config(page_title="apramycin", layout="wide")
st.title("apramycin")
st.markdown(f"PubChem Compound ID: [3081545](https://pubchem.ncbi.nlm.nih.gov/compound/3081545)")
st.markdown(f"IUPAC Name: (2R,3R,4S,5S,6S)-2-[[(2R,3S,4R,4aR,6S,7R,8aS)-7-amino-6-[(1R,2R,3S,4R,6S)-4,6-diamino-2,3-dihydroxycyclohexyl]oxy-4-hydroxy-3-(methylamino)-2,3,4,4a,6,7,8,8a-octahydropyrano[3,2-b]pyran-2-yl]oxy]-5-amino-6-(hydroxymethyl)oxane-3,4-diol")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_3081545.jpg", caption=f"SMILES: CN[C@@H]1[C@@H](O[C@H]2O[C@H](CO)[C@@H](N)[C@H](O)[C@H]2O)O[C@H]2C[C@@H](N)[C@@H](O[C@H]3[C@H](O)[C@@H](O)[C@H](N)C[C@@H]3N)O[C@@H]2[C@@H]1O")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 3081545) ]

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

    