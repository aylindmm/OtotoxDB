
import streamlit as st
import pandas as pd

st.set_page_config(page_title="ouabain", layout="wide")
st.title("ouabain")
st.markdown(f"PubChem Compound ID: [439501](https://pubchem.ncbi.nlm.nih.gov/compound/439501)")
st.markdown(f"IUPAC Name: 3-[(1R,3S,5S,8R,9S,10R,11R,13R,14S,17R)-1,5,11,14-tetrahydroxy-10-(hydroxymethyl)-13-methyl-3-[(2R,3R,4R,5R,6S)-3,4,5-trihydroxy-6-methyloxan-2-yl]oxy-2,3,4,6,7,8,9,11,12,15,16,17-dodecahydro-1H-cyclopenta[a]phenanthren-17-yl]-2H-furan-5-one")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_439501.jpg", caption=f"SMILES: C[C@@H]1O[C@@H](O[C@H]2C[C@@H](O)[C@]3(CO)[C@H]4[C@H](O)C[C@]5(C)[C@@H](C6=CC(=O)OC6)CC[C@]5(O)[C@@H]4CC[C@]3(O)C2)[C@H](O)[C@H](O)[C@H]1O")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 439501) ]

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

    