
import streamlit as st
import pandas as pd

st.set_page_config(page_title="PANCURONIUM BROMIDE", layout="wide")
st.title("PANCURONIUM BROMIDE")
st.markdown(f"PubChem Compound ID: [27350](https://pubchem.ncbi.nlm.nih.gov/compound/27350)")
st.markdown(f"IUPAC Name: [(2S,3S,5S,8R,9S,10S,13S,14S,16S,17R)-17-acetyloxy-10,13-dimethyl-2,16-bis(1-methylpiperidin-1-ium-1-yl)-2,3,4,5,6,7,8,9,11,12,14,15,16,17-tetradecahydro-1H-cyclopenta[a]phenanthren-3-yl] acetate dibromide")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_27350.jpg", caption=f"SMILES: CC(=O)O[C@H]1C[C@@H]2CC[C@@H]3[C@H](CC[C@@]4(C)[C@H]3C[C@H]([N+]3(C)CCCCC3)[C@@H]4OC(C)=O)[C@@]2(C)C[C@@H]1[N+]1(C)CCCCC1")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 27350) ]

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

    