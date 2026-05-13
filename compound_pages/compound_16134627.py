
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dalbavancin", layout="wide")
st.title("Dalbavancin")
# Display the image in Streamlit
st.image(f"compound_structures/compound_16134627.jpg", width=300)
st.markdown(f"PubChem Compound ID: [16134627](https://pubchem.ncbi.nlm.nih.gov/compound/16134627)")
st.markdown(f"IUPAC Name: (2S,3S,4R,5R,6S)-6-[[(1S,2R,19R,22R,34S,37R,40R,52S)-5,32-dichloro-52-[3-(dimethylamino)propylcarbamoyl]-2,26,31,44,49-pentahydroxy-22-(methylamino)-21,35,38,54,56,59-hexaoxo-47-[(2R,3S,4S,5S,6R)-3,4,5-trihydroxy-6-(hydroxymethyl)oxan-2-yl]oxy-7,13,28-trioxa-20,36,39,53,55,58-hexazaundecacyclo[38.14.2.23,6.214,17.219,34.18,12.123,27.129,33.141,45.010,37.046,51]hexahexaconta-3,5,8,10,12(64),14(63),15,17(62),23(61),24,26,29(60),30,32,41(57),42,44,46(51),47,49,65-henicosaen-64-yl]oxy]-3,4-dihydroxy-5-(10-methylundecanoylamino)oxane-2-carboxylic acid")
st.markdown(f"Score: 0.0134498991257566")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 16134627) ]

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

    