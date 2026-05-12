
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Rifampicin", layout="wide")
st.title("Rifampicin")
st.markdown(f"PubChem Compound ID: [135398735](https://pubchem.ncbi.nlm.nih.gov/compound/135398735)")
st.markdown(f"IUPAC Name: [(7S,9E,11S,12R,13S,14R,15R,16R,17S,18S,19E,21Z)-2,15,17,27,29-pentahydroxy-11-methoxy-3,7,12,14,16,18,22-heptamethyl-26-[(E)-(4-methylpiperazin-1-yl)iminomethyl]-6,23-dioxo-8,30-dioxa-24-azatetracyclo[23.3.1.14,7.05,28]triaconta-1(29),2,4,9,19,21,25,27-octaen-13-yl] acetate")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_135398735.jpg", caption=f"SMILES: CO[C@H]1/C=C/O[C@@]2(C)Oc3c(C)c(O)c4c(O)c(c(C=NN5CCN(C)CC5)c(O)c4c3C2=O)NC(=O)C(C)=CC=CC(C)[C@H](O)[C@@H](C)[C@@H](O)[C@@H](C)[C@H](OC(C)=O)[C@@H]1C")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 135398735) ]

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

    