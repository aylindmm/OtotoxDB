
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Plazomicin", layout="wide")
st.title("Plazomicin")
# Display the image in Streamlit
st.image(f"compound_structures/compound_42613186.jpg", width=300)
st.markdown(f"PubChem Compound ID: [42613186](https://pubchem.ncbi.nlm.nih.gov/compound/42613186)")
st.markdown(f"IUPAC Name: (2S)-4-amino-N-[(1R,2S,3S,4R,5S)-5-amino-4-[[(2S,3R)-3-amino-6-[(2-hydroxyethylamino)methyl]-3,4-dihydro-2H-pyran-2-yl]oxy]-2-[(2R,3R,4R,5R)-3,5-dihydroxy-5-methyl-4-(methylamino)oxan-2-yl]oxy-3-hydroxycyclohexyl]-2-hydroxybutanamide")
st.markdown(f"Score: 0.0403496973772697")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 42613186) ]


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

    