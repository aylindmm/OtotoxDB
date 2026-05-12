
import streamlit as st
import pandas as pd

st.set_page_config(page_title="62622-76-8", layout="wide")
st.title("62622-76-8")
st.markdown(f"PubChem Compound ID: [196404](https://pubchem.ncbi.nlm.nih.gov/compound/196404)")
st.markdown(f"IUPAC Name: 4-amino-N-[5-amino-4-[3-amino-6-(aminomethyl)-4,5-dihydroxyoxan-2-yl]oxy-3-hydroxy-2-[3-hydroxy-6-methyl-4-(methylamino)oxan-2-yl]oxycyclohexyl]-2-hydroxybutanamide")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_196404.jpg", width=400)

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 196404) ]

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

    