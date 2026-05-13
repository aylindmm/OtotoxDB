
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Vinblastine", layout="wide")
st.title("Vinblastine")
# Display the image in Streamlit
st.image(f"compound_structures/compound_13342.jpg", width=300)
st.markdown(f"PubChem Compound ID: [13342](https://pubchem.ncbi.nlm.nih.gov/compound/13342)")
st.markdown(f"IUPAC Name: methyl (1R,9R,10S,11R,12R,19R)-11-acetyloxy-12-ethyl-4-[(13S,15R,17S)-17-ethyl-17-hydroxy-13-methoxycarbonyl-1,11-diazatetracyclo[13.3.1.04,12.05,10]nonadeca-4(12),5,7,9-tetraen-13-yl]-10-hydroxy-5-methoxy-8-methyl-8,16-diazapentacyclo[10.6.1.01,9.02,7.016,19]nonadeca-2,4,6,13-tetraene-10-carboxylate")
st.markdown(f"Score: 0.0403496973772697")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 13342) ]


df_filtered['PMID'] = df_filtered['PMID'].apply(lambda x: f"https://pubmed.ncbi.nlm.nih.gov/{x}/")  

variable_labels = {
    "ototoxic_drugs": "Ototoxic Reports",
    "otoprotective_drugs": "Otoprotective Reports",
}


for variable in df_filtered['variable'].unique():

    label = variable_labels.get(variable, variable)  # falls back to raw name if not in dict
    st.markdown(f"**{label}**")
    source_df = df_filtered[df_filtered['variable'] == variable]
    st.dataframe(
        source_df[["PMID", "Title", "Year"]].rename(columns={"PMID": "PubMed ID", "Title": "Title", "Year": "Year"}),
        use_container_width=True,
        column_config={
            "PubMed ID": st.column_config.LinkColumn("PubMed ID", display_text="https://pubmed.ncbi.nlm.nih.gov/(.*?)/"),
            "Title": st.column_config.TextColumn("Title"),
        },
        hide_index=True,
    )


st.subheader("Targets")
@st.cache_data
def load_data():
    targets_info = pd.read_csv("data/target_info.tsv", sep='\t')
    return targets_info

target_info = load_data()

tar_filtered = target_info[(target_info["PubChem_CID"] == 13342) ]

tar_filtered['UniProt..SwissProt..Primary.ID.of.Target.Chain'] = tar_filtered['UniProt..SwissProt..Primary.ID.of.Target.Chain'].apply(lambda x: f"https://www.uniprot.org/uniprotkb/{x}/")  
tar_filtered = tar_filtered.loc[:,('Target.Name', 'prot_name','UniProt..SwissProt..Primary.ID.of.Target.Chain', "variable", 'value') ]

for variable in tar_filtered['Target.Name'].unique():

    st.markdown(f"**{variable}**")
    source_df = tar_filtered[tar_filtered['Target.Name'] == variable]
    st.markdown(f"Uniprot ID: [source_df['prot_name'][0]](source_df['UniProt..SwissProt..Primary.ID.of.Target.Chain'][0])")
    st.dataframe(
        source_df[["variable", "value"]].rename(columns={"Variable": "Binding type", "value": "value"}),
        use_container_width=True,
        hide_index=True,
    )



if st.button("Back"):
    st.switch_page("pages/1_Home.py")

    