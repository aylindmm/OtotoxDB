
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Methylnaltrexone", layout="wide")
st.title("Methylnaltrexone")
st.markdown(f"PubChem Compound ID: [5361918](https://pubchem.ncbi.nlm.nih.gov/compound/5361918)")
st.markdown(f"IUPAC Name: (4R,4aS,7aR,12bS)-3-(cyclopropylmethyl)-4a,9-dihydroxy-3-methyl-2,4,5,6,7a,13-hexahydro-1H-4,12-methanobenzofuro[3,2-e]isoquinolin-3-ium-7-one")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_5361918.jpg", caption=f"SMILES: C[N+]1(CC2CC2)CC[C@]23c4c5ccc(O)c4OC2C(=O)CC[C@@]3(O)[C@H]1C5")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 5361918) ]

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

    