
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Clarithromycin", layout="wide")
st.title("Clarithromycin")
# Display the image in Streamlit
st.image(f"compound_structures/compound_84029.jpg", width=300)
st.markdown(f"PubChem Compound ID: [84029](https://pubchem.ncbi.nlm.nih.gov/compound/84029)")
st.markdown(f"IUPAC Name: (3R,4S,5S,6R,7R,9R,11R,12R,13S,14R)-6-[(2S,3R,4S,6R)-4-(dimethylamino)-3-hydroxy-6-methyloxan-2-yl]oxy-14-ethyl-12,13-dihydroxy-4-[(2R,4R,5S,6S)-5-hydroxy-4-methoxy-4,6-dimethyloxan-2-yl]oxy-7-methoxy-3,5,7,9,11,13-hexamethyl-oxacyclotetradecane-2,10-dione")
st.markdown(f"Score: 0.0806993947545393")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 84029) ]

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
        source_df[["PMID", "Title", "Year"]].rename(columns={"PMID": "PubMed ID", "Title": "Title", "Year": "Year"}),
        use_container_width=True,
        column_config={
            "PubMed ID": st.column_config.LinkColumn("PubMed ID", display_text="https://pubmed.ncbi.nlm.nih.gov/(.*?)/"),
            "Title": st.column_config.TextColumn("Title"),
        },
        hide_index=True,
    )


if st.button("Back"):
    st.switch_page("pages/1_Home.py")

    