
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Tacrolimus", layout="wide")
st.title("Tacrolimus")
# Display the image in Streamlit
st.image(f"compound_structures/compound_445643.jpg", width=300)
st.markdown(f"PubChem Compound ID: [445643](https://pubchem.ncbi.nlm.nih.gov/compound/445643)")
st.markdown(f"IUPAC Name: (1R,9S,12S,13R,14S,17R,18E,21S,23S,24R,25S,27R)-1,14-dihydroxy-12-[(E)-1-[(1R,3R,4R)-4-hydroxy-3-methoxycyclohexyl]prop-1-en-2-yl]-23,25-dimethoxy-13,19,21,27-tetramethyl-17-prop-2-enyl-11,28-dioxa-4-azatricyclo[22.3.1.04,9]octacos-18-ene-2,3,10,16-tetrone")
st.markdown(f"Score: 0.0268997982515131")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 445643) ]


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

    