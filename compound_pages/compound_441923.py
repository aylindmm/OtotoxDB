
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Ginsenoside rg1", layout="wide")
st.title("Ginsenoside rg1")
# Display the image in Streamlit
st.image(f"compound_structures/compound_441923.jpg", width=300)
st.markdown(f"PubChem Compound ID: [441923](https://pubchem.ncbi.nlm.nih.gov/compound/441923)")
st.markdown(f"IUPAC Name: (2R,3R,4S,5S,6R)-2-[[(3S,5R,6S,8R,9R,10R,12R,13R,14R,17S)-3,12-dihydroxy-4,4,8,10,14-pentamethyl-17-[(2S)-6-methyl-2-[(2S,3R,4S,5S,6R)-3,4,5-trihydroxy-6-(hydroxymethyl)oxan-2-yl]oxyhept-5-en-2-yl]-2,3,5,6,7,9,11,12,13,15,16,17-dodecahydro-1H-cyclopenta[a]phenanthren-6-yl]oxy]-6-(hydroxymethyl)oxane-3,4,5-triol")
st.markdown(f"Score: -0.0134498991257566")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 441923) ]


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

    