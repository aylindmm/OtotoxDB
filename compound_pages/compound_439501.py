
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Ouabain", layout="wide")
st.title("Ouabain")
# Display the image in Streamlit
st.image(f"compound_structures/compound_439501.jpg", width=300)
st.markdown(f"PubChem Compound ID: [439501](https://pubchem.ncbi.nlm.nih.gov/compound/439501)")
st.markdown(f"IUPAC Name: 3-[(1R,3S,5S,8R,9S,10R,11R,13R,14S,17R)-1,5,11,14-tetrahydroxy-10-(hydroxymethyl)-13-methyl-3-[(2R,3R,4R,5R,6S)-3,4,5-trihydroxy-6-methyloxan-2-yl]oxy-2,3,4,6,7,8,9,11,12,15,16,17-dodecahydro-1H-cyclopenta[a]phenanthren-17-yl]-2H-furan-5-one")
st.markdown(f"Score: 0.0537995965030262")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 439501) ]


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

    