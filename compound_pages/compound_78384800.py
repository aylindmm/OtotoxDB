
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Taxanes", layout="wide")
st.title("Taxanes")
st.markdown(f"PubChem Compound ID: [78384800](https://pubchem.ncbi.nlm.nih.gov/compound/78384800)")
st.markdown(f"IUPAC Name: [11,16-diacetyloxy-2-benzoyloxy-5,8-dihydroxy-3-(2-hydroxypropan-2-yl)-6,10-dimethyl-14-oxatetracyclo[8.6.0.03,7.013,16]hexadec-6-en-9-yl] benzoate")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_78384800.jpg", caption=f"SMILES: CC(=O)OC1CC2OCC2(OC(C)=O)C2C(OC(=O)c3ccccc3)C3(C(C)(C)O)CC(O)C(C)=C3C(O)C(OC(=O)c3ccccc3)C12C")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 78384800) ]

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

    