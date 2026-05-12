
import streamlit as st
import pandas as pd

st.set_page_config(page_title="vitamin B12", layout="wide")
st.title("vitamin B12")
st.markdown(f"PubChem Compound ID: [165339223](https://pubchem.ncbi.nlm.nih.gov/compound/165339223)")
st.markdown(f"IUPAC Name: cobalt(3+);[(2R,3S,5S)-5-(5,6-dimethylbenzimidazol-1-yl)-4-hydroxy-2-(hydroxymethyl)oxolan-3-yl] [(2R)-1-[3-[(1R,2R,3R,4Z,7S,9Z,12S,13S,14Z,17S,18S,19R)-2,13,18-tris(2-amino-2-oxoethyl)-7,12,17-tris(3-amino-3-oxopropyl)-3,5,8,8,13,15,18,19-octamethyl-2,7,12,17-tetrahydro-1H-corrin-21-id-3-yl]propanoylamino]propan-2-yl] phosphate;cyanide")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_165339223.jpg", caption=f"SMILES: CC1=C2[N-][C@H]([C@H](CC(N)=O)[C@@]2(C)CCC(=O)NC[C@@H](C)OP(=O)([O-])O[C@H]2C(O)[C@@H](n3cnc4cc(C)c(C)cc43)O[C@@H]2CO)[C@]2(C)N=C(C(C)=C3N=C(C=C4N=C1[C@@H](CCC(N)=O)C4(C)C)[C@@H](CCC(N)=O)[C@]3(C)CC(N)=O)[C@@H](CCC(N)=O)[C@]2(C)CC(N)=O.[C-]#N.[Co+3]")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 165339223) ]

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

    