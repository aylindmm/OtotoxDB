
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Methyl-|a-cyclodextrin", layout="wide")
st.title("Methyl-|a-cyclodextrin")
st.markdown(f"PubChem Compound ID: [51051622](https://pubchem.ncbi.nlm.nih.gov/compound/51051622)")
st.markdown(f"IUPAC Name: (1S,3R,5R,6R,8R,10R,11R,13R,15R,16R,18R,20R,21R,23R,25R,26R,28R,30R,31S,33R,35R,36R,37S,38R,39S,40R,41S,42R,43S,44R,45S,46R,47S,48R,49S)-5,10,15,20,25,30,35-heptakis(hydroxymethyl)-37,39,40,41,42,43,44,45,46,47,48,49-dodecamethoxy-2,4,7,9,12,14,17,19,22,24,27,29,32,34-tetradecaoxaoctacyclo[31.2.2.23,6.28,11.213,16.218,21.223,26.228,31]nonatetracontane-36,38-diol")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_51051622.jpg", width=400)

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 51051622) ]

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

    