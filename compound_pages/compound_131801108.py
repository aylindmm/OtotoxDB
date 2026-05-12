
import streamlit as st
import pandas as pd

st.set_page_config(page_title="(R)-Azasetron besylate", layout="wide")
st.title("(R)-Azasetron besylate")
st.markdown(f"PubChem Compound ID: [131801108](https://pubchem.ncbi.nlm.nih.gov/compound/131801108)")
st.markdown(f"IUPAC Name: N-[(3R)-1-azabicyclo[2.2.2]octan-3-yl]-6-chloro-4-methyl-3-oxo-1,4-benzoxazine-8-carboxamide;benzenesulfonic acid")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_131801108.jpg", caption=f"SMILES: CN1C(=O)COc2c(C(=O)N[C@H]3CN4CCC3CC4)cc(Cl)cc21.O=S(=O)(O)c1ccccc1")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 131801108) ]

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

    