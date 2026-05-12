
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Tirilazad mesylate", layout="wide")
st.title("Tirilazad mesylate")
st.markdown(f"PubChem Compound ID: [104902](https://pubchem.ncbi.nlm.nih.gov/compound/104902)")
st.markdown(f"IUPAC Name: (8S,10S,13S,14S,16R,17S)-17-[2-[4-(2,6-dipyrrolidin-1-ylpyrimidin-4-yl)piperazin-1-yl]acetyl]-10,13,16-trimethyl-6,7,8,12,14,15,16,17-octahydrocyclopenta[a]phenanthren-3-one;methanesulfonic acid")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_104902.jpg", caption=f"SMILES: C[C@@H]1C[C@H]2[C@@H]3CC=C4CC(=O)C=C[C@]4(C)C3=CC[C@]2(C)C1C(=O)CN1CCN(c2cc(N3CCCC3)nc(N3CCCC3)n2)CC1")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 104902) ]

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

    