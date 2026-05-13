
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Rifamycin", layout="wide")
st.title("Rifamycin")
# Display the image in Streamlit
st.image(f"compound_structures/compound_6324616.jpg", width=300)
st.markdown(f"PubChem Compound ID: [6324616](https://pubchem.ncbi.nlm.nih.gov/compound/6324616)")
st.markdown(f"IUPAC Name: [(7S,9E,11S,12R,13S,14R,15R,16R,17S,18S,19E,21Z)-2,15,17,27,29-pentahydroxy-11-methoxy-3,7,12,14,16,18,22-heptamethyl-6,23-dioxo-8,30-dioxa-24-azatetracyclo[23.3.1.14,7.05,28]triaconta-1(29),2,4,9,19,21,25,27-octaen-13-yl] acetate")
st.markdown(f"Score: 0.0134498991257566")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 6324616) ]


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

    