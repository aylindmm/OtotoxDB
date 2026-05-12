
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Cyclodextrin", layout="wide")
st.title("Cyclodextrin")
st.markdown(f"PubChem Compound ID: [320760](https://pubchem.ncbi.nlm.nih.gov/compound/320760)")
st.markdown(f"IUPAC Name: 5,10,15,20,25,30-hexakis(hydroxymethyl)-2,4,7,9,12,14,17,19,22,24,27,29-dodecaoxaheptacyclo[26.2.2.23,6.28,11.213,16.218,21.223,26]dotetracontane-31,32,33,34,35,36,37,38,39,40,41,42-dodecol")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_320760.jpg", width=400)

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 320760) ]

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

    