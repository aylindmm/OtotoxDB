
import streamlit as st
import pandas as pd

st.set_page_config(page_title="HYDROXOCOBALAMIN", layout="wide")
st.title("HYDROXOCOBALAMIN")
st.markdown(f"PubChem Compound ID: [44475014](https://pubchem.ncbi.nlm.nih.gov/compound/44475014)")
st.markdown(f"IUPAC Name: cobalt(3+);[(2R,3S,4R,5S)-5-(5,6-dimethylbenzimidazol-1-yl)-4-hydroxy-2-(hydroxymethyl)oxolan-3-yl] [(2R)-1-[3-[(1R,2R,3R,4Z,7S,9Z,12S,13S,14Z,17S,18S,19R)-2,13,18-tris(2-amino-2-oxoethyl)-7,12,17-tris(3-amino-3-oxopropyl)-3,5,8,8,13,15,18,19-octamethyl-2,7,12,17-tetrahydro-1H-corrin-21-id-3-yl]propanoylamino]propan-2-yl] phosphate;hydroxide")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_44475014.jpg", caption=f"SMILES: CC1=C2N=C(C=C3N=C(C(C)=C4N[C@@](C)([C@@H]5N=C1[C@](C)(CCC(=O)NC[C@@H](C)OP(=O)(O)O[C@H]1[C@@H](O)[C@@H](n6cnc7cc(C)c(C)cc76)O[C@@H]1CO)[C@H]5CC(N)=O)[C@@](C)(CC(N)=O)[C@@H]4CCC(N)=O)[C@@](C)(CC(N)=O)[C@@H]3CCC(N)=O)C(C)(C)[C@@H]2CCC(N)=O.[Co+3]")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 44475014) ]

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

    