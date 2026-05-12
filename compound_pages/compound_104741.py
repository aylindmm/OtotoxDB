
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Fulvestrant", layout="wide")
st.title("Fulvestrant")
st.markdown(f"PubChem Compound ID: [104741](https://pubchem.ncbi.nlm.nih.gov/compound/104741)")
st.markdown(f"IUPAC Name: (7R,8R,9S,13S,14S,17S)-13-methyl-7-[9-(4,4,5,5,5-pentafluoropentylsulfinyl)nonyl]-6,7,8,9,11,12,14,15,16,17-decahydrocyclopenta[a]phenanthrene-3,17-diol")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_104741.jpg", caption=f"SMILES: C[C@]12CC[C@@H]3c4ccc(O)cc4C[C@@H](CCCCCCCCCS(=O)CCCC(F)(F)C(F)(F)F)[C@H]3[C@@H]1CC[C@@H]2O")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 104741) ]

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

    