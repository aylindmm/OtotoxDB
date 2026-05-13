
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Bilobalide", layout="wide")
st.title("Bilobalide")
# Display the image in Streamlit
st.image(f"compound_structures/compound_73581.jpg", width=300)
st.markdown(f"PubChem Compound ID: [73581](https://pubchem.ncbi.nlm.nih.gov/compound/73581)")
st.markdown(f"IUPAC Name: (1S,4R,7R,8S,9R,11S)-9-tert-butyl-7,9-dihydroxy-3,5,12-trioxatetracyclo[6.6.0.01,11.04,8]tetradecane-2,6,13-trione")
st.markdown(f"Score: -0.0134498991257566")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 73581) ]


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

    