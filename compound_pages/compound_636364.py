
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dibekacin sulfate", layout="wide")
st.title("Dibekacin sulfate")
# Display the image in Streamlit
st.image(f"compound_structures/compound_636364.jpg", width=300)
st.markdown(f"PubChem Compound ID: [636364](https://pubchem.ncbi.nlm.nih.gov/compound/636364)")
st.markdown(f"IUPAC Name: (2S,3R,4S,5S,6R)-4-amino-2-[(1S,2S,3R,4S,6R)-4,6-diamino-3-[(2R,3R,6S)-3-amino-6-(aminomethyl)oxan-2-yl]oxy-2-hydroxycyclohexyl]oxy-6-(hydroxymethyl)oxane-3,5-diol;sulfuric acid")
st.markdown(f"Score: 0.0268997982515131")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 636364) ]

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

    