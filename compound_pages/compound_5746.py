
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Mitomycin c", layout="wide")
st.title("Mitomycin c")
# Display the image in Streamlit
st.image(f"compound_structures/compound_5746.jpg", width=300)
st.markdown(f"PubChem Compound ID: [5746](https://pubchem.ncbi.nlm.nih.gov/compound/5746)")
st.markdown(f"IUPAC Name: [(4S,6S,7R,8S)-11-amino-7-methoxy-12-methyl-10,13-dioxo-2,5-diazatetracyclo[7.4.0.02,7.04,6]trideca-1(9),11-dien-8-yl]methyl carbamate")
st.markdown(f"Score: 0.0")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 5746) ]

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

    