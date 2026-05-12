
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Ginkgolide B", layout="wide")
st.title("Ginkgolide B")
st.markdown(f"PubChem Compound ID: [11973122](https://pubchem.ncbi.nlm.nih.gov/compound/11973122)")
st.markdown(f"IUPAC Name: (1R,3R,6R,7S,8S,10R,11R,12S,13S,16S,17R)-8-tert-butyl-6,12,17-trihydroxy-16-methyl-2,4,14,19-tetraoxahexacyclo[8.7.2.01,11.03,7.07,11.013,17]nonadecane-5,15,18-trione")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_11973122.jpg", caption=f"SMILES: CC1C(=O)O[C@H]2[C@@H](O)[C@@]34[C@H]5C[C@@H](C(C)(C)C)[C@@]36C(O)C(=O)O[C@H]6O[C@@]4(C(=O)O5)[C@@]12O")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 11973122) ]

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

    