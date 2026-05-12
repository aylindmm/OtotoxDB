
import streamlit as st
import pandas as pd

st.set_page_config(page_title="lincomycin", layout="wide")
st.title("lincomycin")
st.markdown(f"PubChem Compound ID: [3000540](https://pubchem.ncbi.nlm.nih.gov/compound/3000540)")
st.markdown(f"IUPAC Name: (2S,4R)-N-[(1R,2R)-2-hydroxy-1-[(2R,3R,4S,5R,6R)-3,4,5-trihydroxy-6-methylsulfanyloxan-2-yl]propyl]-1-methyl-4-propylpyrrolidine-2-carboxamide")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_3000540.jpg", caption=f"SMILES: CCC[C@@H]1CC(C(=O)N[C@@H]([C@H]2O[C@H](SC)[C@H](O)[C@@H](O)[C@H]2O)[C@@H](C)O)N(C)C1")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 3000540) ]

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

    