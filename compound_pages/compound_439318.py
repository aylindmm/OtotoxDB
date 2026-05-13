
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Bekanamycin", layout="wide")
st.title("Bekanamycin")
# Display the image in Streamlit
st.image(f"compound_structures/compound_439318.jpg", width=300)
st.markdown(f"PubChem Compound ID: [439318](https://pubchem.ncbi.nlm.nih.gov/compound/439318)")
st.markdown(f"IUPAC Name: (2R,3S,4R,5R,6R)-5-amino-2-(aminomethyl)-6-[(1R,2S,3S,4R,6S)-4,6-diamino-3-[(2S,3R,4S,5S,6R)-4-amino-3,5-dihydroxy-6-(hydroxymethyl)oxan-2-yl]oxy-2-hydroxycyclohexyl]oxyoxane-3,4-diol")
st.markdown(f"Score: 0.0268997982515131")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 439318) ]


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

    