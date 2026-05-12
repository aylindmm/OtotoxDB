
import streamlit as st
import pandas as pd

st.set_page_config(page_title="3-[(4-AMINO-1-TERT-BUTYL-1H-PYRAZOLO[3,4-D]PYRIMIDIN-3-YL)METHYL]PHENOL", layout="wide")
st.title("3-[(4-AMINO-1-TERT-BUTYL-1H-PYRAZOLO[3,4-D]PYRIMIDIN-3-YL)METHYL]PHENOL")
st.markdown(f"PubChem Compound ID: [16750071](https://pubchem.ncbi.nlm.nih.gov/compound/16750071)")
st.markdown(f"IUPAC Name: 3-[(4-amino-1-tert-butylpyrazolo[3,4-d]pyrimidin-3-yl)methyl]phenol")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_16750071.jpg", caption=f"SMILES: CC(C)(C)n1nc(Cc2cccc(O)c2)c2c(N)ncnc21")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 16750071) ]

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

    