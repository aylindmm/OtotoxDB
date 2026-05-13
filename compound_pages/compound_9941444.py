
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Pasireotide", layout="wide")
st.title("Pasireotide")
# Display the image in Streamlit
st.image(f"compound_structures/compound_9941444.jpg", width=300)
st.markdown(f"PubChem Compound ID: [9941444](https://pubchem.ncbi.nlm.nih.gov/compound/9941444)")
st.markdown(f"IUPAC Name: [(3S,6S,9S,12R,15S,18S,20R)-9-(4-aminobutyl)-3-benzyl-12-(1H-indol-3-ylmethyl)-2,5,8,11,14,17-hexaoxo-15-phenyl-6-[(4-phenylmethoxyphenyl)methyl]-1,4,7,10,13,16-hexazabicyclo[16.3.0]henicosan-20-yl] N-(2-aminoethyl)carbamate")
st.markdown(f"Score: -0.0268997982515131")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 9941444) ]

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

    