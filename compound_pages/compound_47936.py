
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Forskolin", layout="wide")
st.title("Forskolin")
st.markdown(f"PubChem Compound ID: [47936](https://pubchem.ncbi.nlm.nih.gov/compound/47936)")
st.markdown(f"IUPAC Name: [(3R,4aR,5S,6S,6aS,10S,10aR,10bS)-3-ethenyl-6,10,10b-trihydroxy-3,4a,7,7,10a-pentamethyl-1-oxo-5,6,6a,8,9,10-hexahydro-2H-benzo[f]chromen-5-yl] acetate")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_47936.jpg", width=400)

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 47936) ]

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

    