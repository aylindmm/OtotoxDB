
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Norvancomycin", layout="wide")
st.title("Norvancomycin")
# Display the image in Streamlit
st.image(f"compound_structures/compound_10419027.jpg", width=300)
st.markdown(f"PubChem Compound ID: [10419027](https://pubchem.ncbi.nlm.nih.gov/compound/10419027)")
st.markdown(f"IUPAC Name: (1S,2R,18R,19R,22S,25R,28R,40S)-48-[(2S,3R,4S,5S,6R)-3-[(2S,4S,5S,6S)-4-amino-5-hydroxy-4,6-dimethyloxan-2-yl]oxy-4,5-dihydroxy-6-(hydroxymethyl)oxan-2-yl]oxy-19-[[(2R)-2-amino-4-methylpentanoyl]amino]-22-(2-amino-2-oxoethyl)-5,15-dichloro-2,18,32,35,37-pentahydroxy-20,23,26,42,44-pentaoxo-7,13-dioxa-21,24,27,41,43-pentazaoctacyclo[26.14.2.23,6.214,17.18,12.129,33.010,25.034,39]pentaconta-3,5,8(48),9,11,14,16,29(45),30,32,34(39),35,37,46,49-pentadecaene-40-carboxylic acid")
st.markdown(f"Score: 0.0134498991257566")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 10419027) ]


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

    