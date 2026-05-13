
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Minerval", layout="wide")
st.title("Minerval")
# Display the image in Streamlit
st.image(f"compound_structures/compound_9796304.jpg", width=300)
st.markdown(f"PubChem Compound ID: [9796304](https://pubchem.ncbi.nlm.nih.gov/compound/9796304)")
st.markdown(f"IUPAC Name: (Z)-2-hydroxyoctadec-9-enoic acid")
st.markdown(f"Score: -0.0134498991257566")
st.markdown(f"Classification: otoprotective")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 9796304) ]


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

tar_filtered = target_info[(target_info["PubChem_CID"] == 9796304) ]

tar_filtered['UniProt..SwissProt..Primary.ID.of.Target.Chain'] = tar_filtered['UniProt..SwissProt..Primary.ID.of.Target.Chain'].apply(lambda x: f"https://www.uniprot.org/uniprotkb/{x}/")  
tar_filtered = tar_filtered.loc[:,('Target.Name', 'prot_name','UniProt..SwissProt..Primary.ID.of.Target.Chain', "variable", 'value') ]

if tar_filtered.empty:
    st.info("No target information available for this compound.")
else:
    for variable in tar_filtered['Target.Name'].unique():
        st.markdown(f"**{variable}**")
        source_df = tar_filtered[tar_filtered['Target.Name'] == variable]
        st.markdown(f"Uniprot ID: " [source_df['prot_name'][0]](source_df['UniProt..SwissProt..Primary.ID.of.Target.Chain'][0]))

        if not source_df.empty:
            st.dataframe(
                source_df[["variable", "value"]].rename(columns={"Variable": "Binding type", "value": "value"}),
                use_container_width=True,
                hide_index=True,
            )
if st.button("Back"):
    st.switch_page("pages/1_Home.py")

    