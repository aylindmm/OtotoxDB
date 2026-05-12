
import streamlit as st
import pandas as pd

st.set_page_config(page_title="geldanamycin", layout="wide")
st.title("geldanamycin")
st.markdown(f"PubChem Compound ID: [5288382](https://pubchem.ncbi.nlm.nih.gov/compound/5288382)")
st.markdown(f"IUPAC Name: [(4E,6Z,8S,9S,10E,12S,13R,14S,16R)-13-hydroxy-8,14,19-trimethoxy-4,10,12,16-tetramethyl-3,20,22-trioxo-2-azabicyclo[16.3.1]docosa-1(21),4,6,10,18-pentaen-9-yl] carbamate")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_5288382.jpg", caption=f"SMILES: COc1c(O)cc2c(O)c1C=C(C)C[C@H](OC)[C@H](O)[C@@H](C)/C=C(\C)[C@H](OC(N)=O)[C@@H](OC)C=CC=C(C)C(=O)N2")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 5288382) ]

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

    