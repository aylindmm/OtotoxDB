
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Ivermectin b1a", layout="wide")
st.title("Ivermectin b1a")
st.markdown(f"PubChem Compound ID: [6321424](https://pubchem.ncbi.nlm.nih.gov/compound/6321424)")
st.markdown(f"IUPAC Name: (1R,4S,5'S,6R,6'R,8R,10E,12S,13S,14E,16E,20R,21R,24S)-6'-[(2S)-butan-2-yl]-21,24-dihydroxy-12-[(2R,4S,5S,6S)-5-[(2S,4S,5S,6S)-5-hydroxy-4-methoxy-6-methyloxan-2-yl]oxy-4-methoxy-6-methyloxan-2-yl]oxy-5',11,13,22-tetramethylspiro[3,7,19-trioxatetracyclo[15.6.1.14,8.020,24]pentacosa-10,14,16,22-tetraene-6,2'-oxane]-2-one")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_6321424.jpg", width=400)

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 6321424) ]

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

    