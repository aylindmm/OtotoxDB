
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Oridonin", layout="wide")
st.title("Oridonin")
st.markdown(f"PubChem Compound ID: [5321010](https://pubchem.ncbi.nlm.nih.gov/compound/5321010)")
st.markdown(f"IUPAC Name: (1S,2S,5S,8R,9S,10S,11R,15S,18R)-9,10,15,18-tetrahydroxy-12,12-dimethyl-6-methylidene-17-oxapentacyclo[7.6.2.15,8.01,11.02,8]octadecan-7-one")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_5321010.jpg", caption=f"SMILES: C=C1C(=O)[C@]23[C@H](O)[C@H]1CC[C@H]2[C@@]12CO[C@]3(O)[C@@H](O)[C@@H]1C(C)(C)CC[C@@H]2O")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 5321010) ]

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

    