
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Colimycine", layout="wide")
st.title("Colimycine")
# Display the image in Streamlit
st.image(f"compound_structures/compound_44585614.jpg", width=300)
st.markdown(f"PubChem Compound ID: [44585614](https://pubchem.ncbi.nlm.nih.gov/compound/44585614)")
st.markdown(f"IUPAC Name: 6-methyl-N-[2-[(2S,5S,8S,11S,14S,17S,20S,23S)-8,11,14,20-tetrakis(2-aminoethyl)-5-[(1R)-1-hydroxyethyl]-17,23-bis(2-methylpropyl)-3,6,9,12,15,18,21,24-octaoxo-1,4,7,10,13,16,19,22-octazacyclotetracos-2-yl]ethyl]octanamide")
st.markdown(f"Score: 0.0134498991257566")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 44585614) ]


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

    