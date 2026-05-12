
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Butorphanol", layout="wide")
st.title("Butorphanol")
st.markdown(f"PubChem Compound ID: [5361092](https://pubchem.ncbi.nlm.nih.gov/compound/5361092)")
st.markdown(f"IUPAC Name: (1S,9R,10S)-17-(cyclobutylmethyl)-17-azatetracyclo[7.5.3.01,10.02,7]heptadeca-2(7),3,5-triene-4,10-diol")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_5361092.jpg", width=400)

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 5361092) ]

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

    