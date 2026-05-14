
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Caspofungin", layout="wide")
st.title("Caspofungin")
# Display the image in Streamlit
st.image(f"compound_structures/compound_16119814.jpg", width=300)
st.markdown(f"PubChem Compound ID: [16119814](https://pubchem.ncbi.nlm.nih.gov/compound/16119814)")
st.markdown(f"IUPAC Name: (10R,12S)-N-[(3S,6S,9S,11R,15S,18S,20R,21S,24S,25S)-21-(2-aminoethylamino)-3-[(1R)-3-amino-1-hydroxypropyl]-6-[(1S,2S)-1,2-dihydroxy-2-(4-hydroxyphenyl)ethyl]-11,20,25-trihydroxy-15-[(1R)-1-hydroxyethyl]-2,5,8,14,17,23-hexaoxo-1,4,7,13,16,22-hexazatricyclo[22.3.0.09,13]heptacosan-18-yl]-10,12-dimethyltetradecanamide")
st.markdown(f"Score: 0.0084217618325753")
st.markdown(f"Classification: ototoxic")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 16119814) ]


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
        source_df[["PMID", "Year","Title", "dose", "administrarion_route"]].rename(columns={"PMID": "PubMed ID", 
                                                                                        "Title": "Title", 
                                                                                        "Year": "Year",
                                                                                        "dose": "Dose",
                                                                                        "administrarion_route": "Administration route"}),
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

tar_filtered = target_info[(target_info["PubChem_CID"] == 16119814) ]

tar_filtered = tar_filtered.loc[:,('Target.Name', 'prot_name','UniProt..SwissProt..Primary.ID.of.Target.Chain', "variable", 'value') ]

if tar_filtered.empty:
    st.info("No target information available for this compound.")
else:
    for variable in tar_filtered['Target.Name'].unique():
        source_df = tar_filtered[tar_filtered['Target.Name'] == variable]
        uniid = source_df['UniProt..SwissProt..Primary.ID.of.Target.Chain'].iloc[0]
        st.markdown(f"[{variable}](target_{uniid}/)")
        source_df['UniProt..SwissProt..Primary.ID.of.Target.Chain'] = source_df['UniProt..SwissProt..Primary.ID.of.Target.Chain'].apply(lambda x: f"https://www.uniprot.org/uniprotkb/{x}/")

        st.markdown(f"Uniprot ID: [{source_df['prot_name'].iloc[0]}]({source_df['UniProt..SwissProt..Primary.ID.of.Target.Chain'].iloc[0]})")

        st.dataframe(
            source_df[["variable", "value"]].rename(columns={"variable": "Binding type", "value": "Value (nM)"}),
            use_container_width=True,
            hide_index=True,
        )

if st.button("Back"):
    st.switch_page("pages/1_Home.py")

    