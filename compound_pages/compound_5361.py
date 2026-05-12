
import streamlit as st
import pandas as pd

st.set_page_config(page_title="suramin", layout="wide")
st.title("suramin")
st.markdown(f"PubChem Compound ID: [5361](https://pubchem.ncbi.nlm.nih.gov/compound/5361)")
st.markdown(f"IUPAC Name: 8-[[4-methyl-3-[[3-[[3-[[2-methyl-5-[(4,6,8-trisulfonaphthalen-1-yl)carbamoyl]phenyl]carbamoyl]phenyl]carbamoylamino]benzoyl]amino]benzoyl]amino]naphthalene-1,3,5-trisulfonic acid")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_5361.jpg", caption=f"SMILES: Cc1ccc(C(=O)Nc2ccc(S(=O)(=O)O)c3cc(S(=O)(=O)O)cc(S(=O)(=O)O)c23)cc1NC(=O)c1cccc(NC(=O)Nc2cccc(C(=O)Nc3cc(C(=O)Nc4ccc(S(=O)(=O)O)c5cc(S(=O)(=O)O)cc(S(=O)(=O)O)c45)ccc3C)c2)c1")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 5361) ]

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

    