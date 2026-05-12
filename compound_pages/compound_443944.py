
import streamlit as st
import pandas as pd

st.set_page_config(page_title="metrizamide", layout="wide")
st.title("metrizamide")
st.markdown(f"PubChem Compound ID: [443944](https://pubchem.ncbi.nlm.nih.gov/compound/443944)")
st.markdown(f"IUPAC Name: 3-acetamido-5-[acetyl(methyl)amino]-2,4,6-triiodo-N-[(3R,4R,5S,6R)-2,4,5-trihydroxy-6-(hydroxymethyl)oxan-3-yl]benzamide")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_443944.jpg", caption=f"SMILES: CC(=O)Nc1c(I)c(C(=O)N[C@H]2C(O)O[C@H](CO)[C@@H](O)[C@@H]2O)c(I)c(N(C)C(C)=O)c1I")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 443944) ]

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

    