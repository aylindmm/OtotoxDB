
import streamlit as st
import pandas as pd

st.set_page_config(page_title="2097416-76-5", layout="wide")
st.title("2097416-76-5")
st.markdown(f"PubChem Compound ID: [129116690](https://pubchem.ncbi.nlm.nih.gov/compound/129116690)")
st.markdown(f"IUPAC Name: (6R)-7-[(3,4-difluorophenyl)methyl]-6-(methoxymethyl)-2-[5-methyl-2-[(2-methylpyrazol-3-yl)amino]pyrimidin-4-yl]-5,6-dihydroimidazo[1,2-a]pyrazin-8-one")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_129116690.jpg", caption=f"SMILES: COC[C@H]1Cn2cc(-c3nc(Nc4ccnn4C)ncc3C)nc2C(=O)N1Cc1ccc(F)c(F)c1")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 129116690) ]

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

    