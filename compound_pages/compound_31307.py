
import streamlit as st
import pandas as pd

st.set_page_config(page_title="triamcinolone", layout="wide")
st.title("triamcinolone")
st.markdown(f"PubChem Compound ID: [31307](https://pubchem.ncbi.nlm.nih.gov/compound/31307)")
st.markdown(f"IUPAC Name: (8S,9R,10S,11S,13S,14S,16R,17S)-9-fluoro-11,16,17-trihydroxy-17-(2-hydroxyacetyl)-10,13-dimethyl-6,7,8,11,12,14,15,16-octahydrocyclopenta[a]phenanthren-3-one")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_31307.jpg", caption=f"SMILES: C[C@]12C=CC(=O)C=C1CC[C@H]1[C@@H]3C[C@@H](O)[C@](O)(C(=O)CO)[C@@]3(C)C[C@H](O)[C@@]12F")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 31307) ]

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

    