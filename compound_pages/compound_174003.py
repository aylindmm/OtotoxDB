
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Pinoresinol diglucoside", layout="wide")
st.title("Pinoresinol diglucoside")
# Display the image in Streamlit
st.image(f"compound_structures/compound_174003.jpg", width=300)
st.markdown(f"PubChem Compound ID: [174003](https://pubchem.ncbi.nlm.nih.gov/compound/174003)")
st.markdown(f"IUPAC Name: (2S,3R,4S,5S,6R)-2-[4-[(3S,3aR,6S,6aR)-6-[3-methoxy-4-[(2S,3R,4S,5S,6R)-3,4,5-trihydroxy-6-(hydroxymethyl)oxan-2-yl]oxyphenyl]-1,3,3a,4,6,6a-hexahydrofuro[3,4-c]furan-3-yl]-2-methoxyphenoxy]-6-(hydroxymethyl)oxane-3,4,5-triol")
st.markdown(f"Score: -0.0134498991257566")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 174003) ]


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

    