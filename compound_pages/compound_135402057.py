
import streamlit as st
import pandas as pd

st.set_page_config(page_title="noc-5", layout="wide")
st.title("noc-5")
st.markdown(f"PubChem Compound ID: [135402057](https://pubchem.ncbi.nlm.nih.gov/compound/135402057)")
st.markdown(f"IUPAC Name: (Z)-[3-aminopropyl(propan-2-yl)amino]-hydroxyimino-oxidoazanium")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_135402057.jpg", caption=f"SMILES: CC(C)N(CCCN)[N+]([O-])=NO")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 135402057) ]

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

    