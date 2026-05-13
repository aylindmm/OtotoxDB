
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Docetaxel", layout="wide")
st.title("Docetaxel")
# Display the image in Streamlit
st.image(f"compound_structures/compound_148124.jpg", width=300)
st.markdown(f"PubChem Compound ID: [148124](https://pubchem.ncbi.nlm.nih.gov/compound/148124)")
st.markdown(f"IUPAC Name: [(1S,2S,3R,4S,7R,9S,10S,12R,15S)-4-acetyloxy-1,9,12-trihydroxy-15-[(2R,3S)-2-hydroxy-3-[(2-methylpropan-2-yl)oxycarbonylamino]-3-phenylpropanoyl]oxy-10,14,17,17-tetramethyl-11-oxo-6-oxatetracyclo[11.3.1.03,10.04,7]heptadec-13-en-2-yl] benzoate")
st.markdown(f"Score: 0.0268997982515131")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 148124) ]

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

    