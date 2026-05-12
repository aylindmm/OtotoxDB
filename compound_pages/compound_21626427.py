
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Chiisanoside", layout="wide")
st.title("Chiisanoside")
st.markdown(f"PubChem Compound ID: [21626427](https://pubchem.ncbi.nlm.nih.gov/compound/21626427)")
st.markdown(f"IUPAC Name: [(2S,3R,4S,5S,6R)-6-[[(2R,3R,4R,5S,6R)-3,4-dihydroxy-6-(hydroxymethyl)-5-[(2S,3R,4R,5R,6S)-3,4,5-trihydroxy-6-methyloxan-2-yl]oxyoxan-2-yl]oxymethyl]-3,4,5-trihydroxyoxan-2-yl] (1R,2R,5S,8R,9R,10R,12R,16R,17S,18S,21S)-16-hydroxy-1,2,17-trimethyl-14-oxo-8,18-bis(prop-1-en-2-yl)-13-oxapentacyclo[10.8.1.02,10.05,9.017,21]henicosane-5-carboxylate")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_21626427.jpg", width=400)

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 21626427) ]

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

    