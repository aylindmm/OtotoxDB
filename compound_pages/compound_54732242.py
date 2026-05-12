
import streamlit as st
import pandas as pd

st.set_page_config(page_title="NALDEMEDINE", layout="wide")
st.title("NALDEMEDINE")
st.markdown(f"PubChem Compound ID: [54732242](https://pubchem.ncbi.nlm.nih.gov/compound/54732242)")
st.markdown(f"IUPAC Name: (4R,4aS,7aR,12bS)-3-(cyclopropylmethyl)-4a,7,9-trihydroxy-N-[2-(3-phenyl-1,2,4-oxadiazol-5-yl)propan-2-yl]-1,2,4,5,7a,13-hexahydro-4,12-methanobenzofuro[3,2-e]isoquinoline-6-carboxamide")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_54732242.jpg", caption=f"SMILES: CC(C)(NC(=O)C1C[C@@]2(O)[C@H]3Cc4ccc(O)c5c4[C@@]2(CCN3CC2CC2)C(O5)C1=O)c1nc(-c2ccccc2)no1")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 54732242) ]

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

    