
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Apelin-13", layout="wide")
st.title("Apelin-13")
# Display the image in Streamlit
st.image(f"compound_structures/compound_25078060.jpg", width=300)
st.markdown(f"PubChem Compound ID: [25078060](https://pubchem.ncbi.nlm.nih.gov/compound/25078060)")
st.markdown(f"IUPAC Name: (2S)-2-[[(2S)-1-[(2S)-2-[[(2S)-1-[2-[[(2S)-6-amino-2-[[(2S)-2-[[(2S)-2-[[(2S)-2-[[(2S)-5-(diaminomethylideneamino)-2-[[(2S)-1-[(2S)-5-(diaminomethylideneamino)-2-[[(2S)-2,5-diamino-5-oxopentanoyl]amino]pentanoyl]pyrrolidine-2-carbonyl]amino]pentanoyl]amino]-4-methylpentanoyl]amino]-3-hydroxypropanoyl]amino]-3-(1H-imidazol-5-yl)propanoyl]amino]hexanoyl]amino]acetyl]pyrrolidine-2-carbonyl]amino]-4-methylsulfanylbutanoyl]pyrrolidine-2-carbonyl]amino]-3-phenylpropanoic acid")
st.markdown(f"Score: -0.0134498991257566")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 25078060) ]


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

    