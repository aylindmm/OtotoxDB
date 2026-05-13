
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Nimodipine", layout="wide")
st.title("Nimodipine")
# Display the image in Streamlit
st.image(f"compound_structures/compound_4497.jpg", width=300)
st.markdown(f"PubChem Compound ID: [4497](https://pubchem.ncbi.nlm.nih.gov/compound/4497)")
st.markdown(f"IUPAC Name: 3-O-(2-methoxyethyl) 5-O-propan-2-yl 2,6-dimethyl-4-(3-nitrophenyl)-1,4-dihydropyridine-3,5-dicarboxylate")
st.markdown(f"Score: -0.0672494956287828")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 4497) ]

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

    