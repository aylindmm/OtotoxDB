
import streamlit as st
import pandas as pd

st.set_page_config(page_title="VANCOMYCIN", layout="wide")
st.title("VANCOMYCIN")
st.markdown(f"PubChem Compound ID: [14969](https://pubchem.ncbi.nlm.nih.gov/compound/14969)")
st.markdown(f"IUPAC Name: (1S,2R,18R,19R,22S,25R,28R,40S)-48-[(2S,3R,4S,5S,6R)-3-[(2S,4S,5S,6S)-4-amino-5-hydroxy-4,6-dimethyloxan-2-yl]oxy-4,5-dihydroxy-6-(hydroxymethyl)oxan-2-yl]oxy-22-(2-amino-2-oxoethyl)-5,15-dichloro-2,18,32,35,37-pentahydroxy-19-[[(2R)-4-methyl-2-(methylamino)pentanoyl]amino]-20,23,26,42,44-pentaoxo-7,13-dioxa-21,24,27,41,43-pentazaoctacyclo[26.14.2.23,6.214,17.18,12.129,33.010,25.034,39]pentaconta-3,5,8(48),9,11,14,16,29(45),30,32,34(39),35,37,46,49-pentadecaene-40-carboxylic acid")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_14969.jpg", caption=f"SMILES: CNC(CC(C)C)C(=O)NC1C(=O)NC(CC(N)=O)C(=O)NC2C(=O)NC3C(=O)NC(C(=O)NC(C(=O)O)c4cc(O)cc(O)c4-c4cc3ccc4O)[C@H](O)c3ccc(c(Cl)c3)Oc3cc2cc(c3O[C@@H]2O[C@H](CO)[C@@H](O)[C@H](O)[C@H]2O[C@H]2C[C@](C)(N)[C@H](O)[C@H](C)O2)Oc2ccc(cc2Cl)[C@H]1O")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 14969) ]

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

    