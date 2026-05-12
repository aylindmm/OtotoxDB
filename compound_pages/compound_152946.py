
import streamlit as st
import pandas as pd

st.set_page_config(page_title="moxifloxacin", layout="wide")
st.title("moxifloxacin")
st.markdown(f"PubChem Compound ID: [152946](https://pubchem.ncbi.nlm.nih.gov/compound/152946)")
st.markdown(f"IUPAC Name: 7-[(4aS,7aS)-1,2,3,4,4a,5,7,7a-octahydropyrrolo[3,4-b]pyridin-6-yl]-1-cyclopropyl-6-fluoro-8-methoxy-4-oxoquinoline-3-carboxylic acid")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_152946.jpg", caption=f"SMILES: COc1c(N2C[C@@H]3CCCN[C@@H]3C2)c(F)cc2c(=O)c(C(=O)O)cn(C3CC3)c12")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 152946) ]

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

    