
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Vitamin E acid succinate", layout="wide")
st.title("Vitamin E acid succinate")
st.markdown(f"PubChem Compound ID: [425400](https://pubchem.ncbi.nlm.nih.gov/compound/425400)")
st.markdown(f"IUPAC Name: 4-oxo-4-[[2,5,7,8-tetramethyl-2-(4,8,12-trimethyltridecyl)-3,4-dihydrochromen-6-yl]oxy]butanoic acid")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_425400.jpg", caption=f"SMILES: Cc1c(C)c2c(c(C)c1OC(=O)CCC(=O)O)CCC(C)(CCCC(C)CCCC(C)CCCC(C)C)O2")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 425400) ]

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

    