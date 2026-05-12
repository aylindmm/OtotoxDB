
import streamlit as st
import pandas as pd

st.set_page_config(page_title="CABAZITAXEL", layout="wide")
st.title("CABAZITAXEL")
st.markdown(f"PubChem Compound ID: [9854073](https://pubchem.ncbi.nlm.nih.gov/compound/9854073)")
st.markdown(f"IUPAC Name: [(1S,2S,3R,4S,7R,9S,10S,12R,15S)-4-acetyloxy-1-hydroxy-15-[(2R,3S)-2-hydroxy-3-[(2-methylpropan-2-yl)oxycarbonylamino]-3-phenylpropanoyl]oxy-9,12-dimethoxy-10,14,17,17-tetramethyl-11-oxo-6-oxatetracyclo[11.3.1.03,10.04,7]heptadec-13-en-2-yl] benzoate")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_9854073.jpg", caption=f"SMILES: COC1=C2C(C)[C@@H](OC(=O)C(O)C(NC(=O)OC(C)(C)C)c3ccccc3)C[C@@](O)([C@@H](OC(=O)c3ccccc3)[C@@H]3[C@]4(OC(C)=O)CO[C@@H]4C[C@H](OC)[C@@]3(C)C1=O)C2(C)C")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 9854073) ]

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

    