
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Madecassic acid", layout="wide")
st.title("Madecassic acid")
st.markdown(f"PubChem Compound ID: [73412](https://pubchem.ncbi.nlm.nih.gov/compound/73412)")
st.markdown(f"IUPAC Name: (1S,2R,4aS,6aR,6aS,6bR,8R,8aR,9R,10R,11R,12aR,14bS)-8,10,11-trihydroxy-9-(hydroxymethyl)-1,2,6a,6b,9,12a-hexamethyl-2,3,4,5,6,6a,7,8,8a,10,11,12,13,14b-tetradecahydro-1H-picene-4a-carboxylic acid")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_73412.jpg", width=400)

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 73412) ]

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

    