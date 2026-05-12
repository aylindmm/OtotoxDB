
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Isepamicin", layout="wide")
st.title("Isepamicin")
st.markdown(f"PubChem Compound ID: [3037209](https://pubchem.ncbi.nlm.nih.gov/compound/3037209)")
st.markdown(f"IUPAC Name: (2S)-3-amino-N-[(1R,2S,3S,4R,5S)-5-amino-4-[(2R,3R,4S,5S,6R)-6-(aminomethyl)-3,4,5-trihydroxyoxan-2-yl]oxy-2-[(2R,3R,4R,5R)-3,5-dihydroxy-5-methyl-4-(methylamino)oxan-2-yl]oxy-3-hydroxycyclohexyl]-2-hydroxypropanamide")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_3037209.jpg", caption=f"SMILES: CN[C@@H]1[C@@H](O)[C@@H](O[C@@H]2[C@@H](O)[C@H](O[C@H]3O[C@H](CN)[C@@H](O)[C@H](O)[C@H]3O)[C@@H](N)C[C@H]2NC(=O)C(O)CN)OC[C@]1(C)O")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 3037209) ]

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

    