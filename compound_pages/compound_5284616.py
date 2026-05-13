
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Rapamycin", layout="wide")
st.title("Rapamycin")
# Display the image in Streamlit
st.image(f"compound_structures/compound_5284616.jpg", width=300)
st.markdown(f"PubChem Compound ID: [5284616](https://pubchem.ncbi.nlm.nih.gov/compound/5284616)")
st.markdown(f"IUPAC Name: (1R,9S,12S,15R,16E,18R,19R,21R,23S,24E,26E,28E,30S,32S,35R)-1,18-dihydroxy-12-[(2R)-1-[(1S,3R,4R)-4-hydroxy-3-methoxycyclohexyl]propan-2-yl]-19,30-dimethoxy-15,17,21,23,29,35-hexamethyl-11,36-dioxa-4-azatricyclo[30.3.1.04,9]hexatriaconta-16,24,26,28-tetraene-2,3,10,14,20-pentone")
st.markdown(f"Score: -0.147948890383322")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 5284616) ]

# Convert dataframe to CSV
csv = df_filtered.to_csv(index=False, sep='\t').encode('utf-8')

st.download_button(
    label="Download data as TSV",
    data=csv,
    file_name='articles.tsv',
    mime='text/tsv',
)


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
        source_df[["PMID", "Title"]].rename(columns={"PMID": "PubMed ID", "Title": "Title"}),
        use_container_width=True,
        column_config={
            "PubMed ID": st.column_config.LinkColumn("PubMed ID", display_text="https://pubmed.ncbi.nlm.nih.gov/(.*?)/"),
            "Title": st.column_config.TextColumn("Title"),
        },
        hide_index=True,
    )


if st.button("Back"):
    st.switch_page("pages/1_Home.py")

    