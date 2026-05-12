
import streamlit as st
import pandas as pd

st.set_page_config(page_title="CD1530", layout="wide")
st.title("CD1530")
st.markdown(f"PubChem Compound ID: [9952709](https://pubchem.ncbi.nlm.nih.gov/compound/9952709)")
st.markdown(f"IUPAC Name: 4-[7-(1-adamantyl)-6-hydroxynaphthalen-2-yl]benzoic acid")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_9952709.jpg", caption=f"SMILES: O=C(O)c1ccc(-c2ccc3cc(O)c(C45CC6CC(CC(C6)C4)C5)cc3c2)cc1")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 9952709) ]

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

    