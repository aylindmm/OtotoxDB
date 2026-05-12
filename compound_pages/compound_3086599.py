
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Cgs 21680", layout="wide")
st.title("Cgs 21680")
st.markdown(f"PubChem Compound ID: [3086599](https://pubchem.ncbi.nlm.nih.gov/compound/3086599)")
st.markdown(f"IUPAC Name: 3-[4-[2-[[6-amino-9-[(2R,3R,4S,5S)-5-(ethylcarbamoyl)-3,4-dihydroxyoxolan-2-yl]purin-2-yl]amino]ethyl]phenyl]propanoic acid")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_3086599.jpg", caption=f"SMILES: CCNC(=O)C1O[C@@H](n2cnc3c(N)nc(NCCc4ccc(CCC(=O)O)cc4)nc32)[C@H](O)[C@@H]1O")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 3086599) ]

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

    