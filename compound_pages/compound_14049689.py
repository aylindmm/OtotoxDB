
import streamlit as st
import pandas as pd

st.set_page_config(page_title="2 hydroxypropyl beta cyclodextrin", layout="wide")
st.title("2 hydroxypropyl beta cyclodextrin")
# Display the image in Streamlit
st.image(f"compound_structures/compound_14049689.jpg", width=300)
st.markdown(f"PubChem Compound ID: [14049689](https://pubchem.ncbi.nlm.nih.gov/compound/14049689)")
st.markdown(f"IUPAC Name: (1S,3R,5R,6S,8R,10R,11S,13R,15R,16S,18R,20R,21S,23R,25R,26S,28R,30R,31S,33R,35R,36R,37R,38R,39R,40R,41R,42R,43R,44R,45R,46R,47R,48R,49R)-5,10,15,20,25,30,35-heptakis(2-hydroxypropoxymethyl)-2,4,7,9,12,14,17,19,22,24,27,29,32,34-tetradecaoxaoctacyclo[31.2.2.23,6.28,11.213,16.218,21.223,26.228,31]nonatetracontane-36,37,38,39,40,41,42,43,44,45,46,47,48,49-tetradecol")
st.markdown(f"Score: 0.0268997982515131")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 14049689) ]

# Convert dataframe to CSV
csv = df_filtered.to_csv(index=False, sep='\t').encode('utf-8')

st.download_button(
    label="Download data as TSV",
    data=csv,
    file_name='articles.tsv',
    mime='text/tsv',
)


df_filtered['PMID'] = df_filtered['PMID'].apply(lambda x: f"https://pubmed.ncbi.nlm.nih.gov/{x}/")  

variable_labels = {
    "ototoxic_drugs": "Ototoxic Reports",
    "otoprotective_drugs": "Otoprotective Reports",
}


for variable in df_filtered['variable'].unique():

    label = variable_labels.get(variable, variable)  # falls back to raw name if not in dict
    st.markdown(f"**{label}**")
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

    