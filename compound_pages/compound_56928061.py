
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Hygromycin b", layout="wide")
st.title("Hygromycin b")
st.markdown(f"PubChem Compound ID: [56928061](https://pubchem.ncbi.nlm.nih.gov/compound/56928061)")
st.markdown(f"IUPAC Name: (3'R,3aS,4S,4'S,5'R,6R,6'R,7S,7aS)-4-[(1R,2S,3R,5S,6R)-3-amino-2,6-dihydroxy-5-(methylamino)cyclohexyl]oxy-6'-[(1S)-1-amino-2-hydroxyethyl]-6-(hydroxymethyl)spiro[4,6,7,7a-tetrahydro-3aH-[1,3]dioxolo[4,5-c]pyran-2,2'-oxane]-3',4',5',7-tetrol")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_56928061.jpg", width=400)

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 56928061) ]

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

    