
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Baicalin", layout="wide")
st.title("Baicalin")
st.markdown(f"PubChem Compound ID: [64982](https://pubchem.ncbi.nlm.nih.gov/compound/64982)")
st.markdown(f"IUPAC Name: (2S,3S,4S,5R,6S)-6-(5,6-dihydroxy-4-oxo-2-phenylchromen-7-yl)oxy-3,4,5-trihydroxyoxane-2-carboxylic acid")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_64982.jpg", caption=f"SMILES: O=C(O)C1O[C@@H](Oc2cc3oc(-c4ccccc4)cc(=O)c3c(O)c2O)[C@H](O)[C@@H](O)[C@@H]1O")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 64982) ]

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

    