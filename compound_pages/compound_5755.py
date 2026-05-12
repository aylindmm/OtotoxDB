
import streamlit as st
import pandas as pd

st.set_page_config(page_title="prednisolone", layout="wide")
st.title("prednisolone")
st.markdown(f"PubChem Compound ID: [5755](https://pubchem.ncbi.nlm.nih.gov/compound/5755)")
st.markdown(f"IUPAC Name: (8S,9S,10R,11S,13S,14S,17R)-11,17-dihydroxy-17-(2-hydroxyacetyl)-10,13-dimethyl-7,8,9,11,12,14,15,16-octahydro-6H-cyclopenta[a]phenanthren-3-one")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_5755.jpg", caption=f"SMILES: C[C@]12C=CC(=O)C=C1CC[C@@H]1[C@@H]2[C@@H](O)C[C@@]2(C)[C@H]1CC[C@]2(O)C(=O)CO")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 5755) ]

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

    