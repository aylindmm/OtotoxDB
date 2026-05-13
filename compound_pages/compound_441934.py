
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Notoginsenoside r1", layout="wide")
st.title("Notoginsenoside r1")
# Display the image in Streamlit
st.image(f"compound_structures/compound_441934.jpg", width=300)
st.markdown(f"PubChem Compound ID: [441934](https://pubchem.ncbi.nlm.nih.gov/compound/441934)")
st.markdown(f"IUPAC Name: (2S,3R,4S,5S,6R)-2-[(2S)-2-[(3S,5R,6S,8R,9R,10R,12R,13R,14R,17S)-6-[(2R,3R,4S,5S,6R)-4,5-dihydroxy-6-(hydroxymethyl)-3-[(2S,3R,4S,5R)-3,4,5-trihydroxyoxan-2-yl]oxyoxan-2-yl]oxy-3,12-dihydroxy-4,4,8,10,14-pentamethyl-2,3,5,6,7,9,11,12,13,15,16,17-dodecahydro-1H-cyclopenta[a]phenanthren-17-yl]-6-methylhept-5-en-2-yl]oxy-6-(hydroxymethyl)oxane-3,4,5-triol")
st.markdown(f"Score: -0.0134498991257566")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 441934) ]

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

    