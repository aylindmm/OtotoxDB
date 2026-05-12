
import streamlit as st
import pandas as pd

st.set_page_config(page_title="LLY-283", layout="wide")
st.title("LLY-283")
st.markdown(f"PubChem Compound ID: [122669401](https://pubchem.ncbi.nlm.nih.gov/compound/122669401)")
st.markdown(f"IUPAC Name: (2R,3R,4S,5R)-2-(4-aminopyrrolo[2,3-d]pyrimidin-7-yl)-5-[(R)-hydroxy(phenyl)methyl]oxolane-3,4-diol")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_122669401.jpg", caption=f"SMILES: Nc1ncnc2c1ccn2[C@@H]1O[C@H]([C@H](O)c2ccccc2)[C@@H](O)[C@H]1O")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 122669401) ]

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

    