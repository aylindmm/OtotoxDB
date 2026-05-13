
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Alvespimycin", layout="wide")
st.title("Alvespimycin")
# Display the image in Streamlit
st.image(f"compound_structures/compound_5288674.jpg", width=300)
st.markdown(f"PubChem Compound ID: [5288674](https://pubchem.ncbi.nlm.nih.gov/compound/5288674)")
st.markdown(f"IUPAC Name: [(4E,6Z,8S,9S,10E,12S,13R,14S,16R)-19-[2-(dimethylamino)ethylamino]-13-hydroxy-8,14-dimethoxy-4,10,12,16-tetramethyl-3,20,22-trioxo-2-azabicyclo[16.3.1]docosa-1(21),4,6,10,18-pentaen-9-yl] carbamate")
st.markdown(f"Score: -0.0134498991257566")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 5288674) ]

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

    