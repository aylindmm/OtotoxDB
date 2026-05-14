
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Antibiotic 8327a", layout="wide")
st.title("Antibiotic 8327a")
# Display the image in Streamlit
st.image(f"compound_structures/compound_133065662.jpg", width=300)
st.markdown(f"PubChem Compound ID: [133065662](https://pubchem.ncbi.nlm.nih.gov/compound/133065662)")
st.markdown(f"IUPAC Name: (1S,2R,19R,22R,34S,37R,40R,52S)-2-[(2R,3R,4R,5S,6R)-3-acetamido-4,5-dihydroxy-6-(hydroxymethyl)oxan-2-yl]oxy-22-amino-5,15-dichloro-64-[(2S,3R,4R,5S,6R)-3-(decanoylamino)-4,5-dihydroxy-6-(hydroxymethyl)oxan-2-yl]oxy-26,31,44,49-tetrahydroxy-21,35,38,54,56,59-hexaoxo-47-[(3S,4S,5S,6R)-3,4,5-trihydroxy-6-(hydroxymethyl)oxan-2-yl]oxy-7,13,28-trioxa-20,36,39,53,55,58-hexazaundecacyclo[38.14.2.23,6.214,17.219,34.18,12.123,27.129,33.141,45.010,37.046,51]hexahexaconta-3,5,8,10,12(64),14,16,23(61),24,26,29(60),30,32,41(57),42,44,46(51),47,49,62,65-henicosaene-52-carboxylic acid")
st.markdown(f"Score: 0.0806993947545393")
st.markdown(f"Classification: ototoxic")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 133065662) ]


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

tar_filtered = target_info[(target_info["PubChem_CID"] == 133065662) ]

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

    