
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Valganciclovir", layout="wide")
st.title("Valganciclovir")
st.markdown(f"PubChem Compound ID: [135413535](https://pubchem.ncbi.nlm.nih.gov/compound/135413535)")
st.markdown(f"IUPAC Name: [2-[(2-amino-6-oxo-1H-purin-9-yl)methoxy]-3-hydroxypropyl] (2S)-2-amino-3-methylbutanoate")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_135413535.jpg", caption=f"SMILES: CC(C)C(N)C(=O)OCC(CO)OCn1cnc2c(=O)[nH]c(N)nc21")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 135413535) ]

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

    