
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Epoetin alfa", layout="wide")
st.title("Epoetin alfa")
st.markdown(f"PubChem Compound ID: [92043599](https://pubchem.ncbi.nlm.nih.gov/compound/92043599)")
st.markdown(f"IUPAC Name: (4R,5S,6S,7R,9R,10R,11E,13E,16R)-10-[(2R,4R,5S,6S)-4,5-dihydroxy-4,6-dimethyloxan-2-yl]oxy-6-[(2S,3R,4R,5S,6R)-5-[(2R,4R,5S,6S)-4,5-dihydroxy-4,6-dimethyloxan-2-yl]oxy-4-(dimethylamino)-3-hydroxy-6-methyloxan-2-yl]oxy-4-hydroxy-7-(2-hydroxyethyl)-5-methoxy-9,16-dimethyl-1-oxacyclohexadeca-11,13-dien-2-one")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_92043599.jpg", width=400)

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 92043599) ]

# Convert dataframe to CSV
csv = df_filtered.to_csv(index=False, sep='\t').encode('utf-8')

st.download_button(
    label="Download data as TSV",
    data=csv,
    file_name='articles.tsv',
    mime='text/tsv',
)


df_filtered['PMID'] = df_filtered['PMID'].apply(lambda x: f"https://pubmed.ncbi.nlm.nih.gov/{x}/")  

for variable in df_filtered['variable'].unique():
    st.markdown(f"**{variable}**")
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

    