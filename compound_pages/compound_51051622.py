
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Methyl-|a-cyclodextrin", layout="wide")
st.title("Methyl-|a-cyclodextrin")
# Display the image in Streamlit
st.image(f"compound_structures/compound_51051622.jpg", width=300)
st.markdown(f"PubChem Compound ID: [51051622](https://pubchem.ncbi.nlm.nih.gov/compound/51051622)")
st.markdown(f"IUPAC Name: (1S,3R,5R,6R,8R,10R,11R,13R,15R,16R,18R,20R,21R,23R,25R,26R,28R,30R,31S,33R,35R,36R,37S,38R,39S,40R,41S,42R,43S,44R,45S,46R,47S,48R,49S)-5,10,15,20,25,30,35-heptakis(hydroxymethyl)-37,39,40,41,42,43,44,45,46,47,48,49-dodecamethoxy-2,4,7,9,12,14,17,19,22,24,27,29,32,34-tetradecaoxaoctacyclo[31.2.2.23,6.28,11.213,16.218,21.223,26.228,31]nonatetracontane-36,38-diol")
st.markdown(f"Score: 0.0134498991257566")
st.markdown(f"Classification: ototoxic")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 51051622) ]


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

tar_filtered = target_info[(target_info["PubChem_CID"] == 51051622) ]

tar_filtered['UniProt..SwissProt..Primary.ID.of.Target.Chain'] = tar_filtered['UniProt..SwissProt..Primary.ID.of.Target.Chain'].apply(lambda x: f"https://www.uniprot.org/uniprotkb/{x}/")  
tar_filtered = tar_filtered.loc[:,('Target.Name', 'prot_name','UniProt..SwissProt..Primary.ID.of.Target.Chain', "variable", 'value') ]

if tar_filtered.empty:
    st.info("No target information available for this compound.")
else:
    for variable in tar_filtered['Target.Name'].unique():
        st.markdown(f"**{variable}**")
        source_df = tar_filtered[tar_filtered['Target.Name'] == variable]
        st.markdown(f"Uniprot ID: [{source_df['prot_name'].iloc[0]}]({source_df['UniProt..SwissProt..Primary.ID.of.Target.Chain'].iloc[0]})")


        if not source_df.empty:
            st.dataframe(
                source_df[["variable", "value"]].rename(columns={"Variable": "Binding type", "value": "value"}),
                use_container_width=True,
                hide_index=True,
            )
if st.button("Back"):
    st.switch_page("pages/1_Home.py")

    