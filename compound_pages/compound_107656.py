
import streamlit as st
import pandas as pd

st.set_page_config(page_title="133681-84-2", layout="wide")
st.title("133681-84-2")
st.markdown(f"PubChem Compound ID: [107656](https://pubchem.ncbi.nlm.nih.gov/compound/107656)")
st.markdown(f"IUPAC Name: 2-[[4-(2,6-dipyrrolidin-1-ylpyrimidin-4-yl)piperazin-1-yl]methyl]-2,5,7,8-tetramethyl-3,4-dihydrochromen-6-ol;dihydrochloride")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_107656.jpg", caption=f"SMILES: Cc1c(C)c2c(c(C)c1O)CCC(C)(CN1CCN(c3cc(N4CCCC4)nc(N4CCCC4)n3)CC1)O2")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 107656) ]

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

    