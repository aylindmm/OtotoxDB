
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Cilastatin", layout="wide")
st.title("Cilastatin")
# Display the image in Streamlit
st.image(f"compound_structures/compound_6435415.jpg", width=300)
st.markdown(f"PubChem Compound ID: [6435415](https://pubchem.ncbi.nlm.nih.gov/compound/6435415)")
st.markdown(f"IUPAC Name: (Z)-7-[(2R)-2-amino-2-carboxyethyl]sulfanyl-2-[[(1S)-2,2-dimethylcyclopropanecarbonyl]amino]hept-2-enoic acid")
st.markdown(f"Score: -0.0134498991257566")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 6435415) ]


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

    