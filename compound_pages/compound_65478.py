
import streamlit as st
import pandas as pd

st.set_page_config(page_title="151-73-5", layout="wide")
st.title("151-73-5")
st.markdown(f"PubChem Compound ID: [65478](https://pubchem.ncbi.nlm.nih.gov/compound/65478)")
st.markdown(f"IUPAC Name: disodium;[2-[(8S,9R,10S,11S,13S,14S,16S,17R)-9-fluoro-11,17-dihydroxy-10,13,16-trimethyl-3-oxo-6,7,8,11,12,14,15,16-octahydrocyclopenta[a]phenanthren-17-yl]-2-oxoethyl] phosphate")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_65478.jpg", caption=f"SMILES: C[C@H]1C[C@H]2[C@@H]3CC=C4CC(=O)C=C[C@]4(C)[C@@]3(F)[C@@H](O)C[C@]2(C)[C@@]1(O)C(=O)COP(=O)(O)O")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 65478) ]

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

    