
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Teniposide", layout="wide")
st.title("Teniposide")
st.markdown(f"PubChem Compound ID: [452548](https://pubchem.ncbi.nlm.nih.gov/compound/452548)")
st.markdown(f"IUPAC Name: (5S,5aR,8aR,9R)-5-[[(2R,4aR,6R,7R,8R,8aS)-7,8-dihydroxy-2-thiophen-2-yl-4,4a,6,7,8,8a-hexahydropyrano[3,2-d][1,3]dioxin-6-yl]oxy]-9-(4-hydroxy-3,5-dimethoxyphenyl)-5a,6,8a,9-tetrahydro-5H-[2]benzofuro[6,5-f][1,3]benzodioxol-8-one")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_452548.jpg", width=400)

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 452548) ]

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

    