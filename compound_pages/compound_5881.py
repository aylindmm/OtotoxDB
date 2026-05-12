
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dehydroepiandrosterone", layout="wide")
st.title("Dehydroepiandrosterone")
st.markdown(f"PubChem Compound ID: [5881](https://pubchem.ncbi.nlm.nih.gov/compound/5881)")
st.markdown(f"IUPAC Name: (3S,8R,9S,10R,13S,14S)-3-hydroxy-10,13-dimethyl-1,2,3,4,7,8,9,11,12,14,15,16-dodecahydrocyclopenta[a]phenanthren-17-one")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_5881.jpg", caption=f"SMILES: C[C@]12CC[C@H](O)CC1=CC[C@@H]1[C@@H]2CC[C@]2(C)C(=O)CC[C@@H]12")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 5881) ]

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

    