import streamlit as st
import base64
import pandas as pd

# Show the page title and description.
st.set_page_config(page_title="Compounds", page_icon="🥗")
st.title("Compounds")
st.write(
    """
All compounds found in the literature to have an effect on ototoxicity. The data is collected from scientific publications and includes information on the compound name, source, epigenetic mechanism affected, and the observed effects. This database serves as a resource for researchers and practitioners interested in the field of ototoxicity and its potential applications in health and disease management.
"""
)
#st.cache_data.clear()
# Load the data from a CSV. We're caching this so it doesn't reload every time the app
# reruns (e.g. if the user interacts with the widgets).
@st.cache_data
def load_data():
    df = pd.read_csv("data/compounds.tsv", sep="\t")
    return df


df = load_data()
df['link_to_compound_page'] = df['PubChem_CID']
df['PubChem_CID'] = df['PubChem_CID'].apply(lambda x: f"https://pubchem.ncbi.nlm.nih.gov/compound/{x}" if pd.notnull(x) else x)
df['link_to_compound_page'] = df.apply(lambda row: f"compound_{row['PubChem_CID'].split('/')[-1]}", axis=1)


# Split dietary sources into list

# Define a function to convert an image to base64
def get_base64_image(image_path):
    with open(image_path, "rb") as f:
        data = f.read()
    base64_str = base64.b64encode(data).decode()
    return f"data:image/png;base64,{base64_str}"

df['link_to_image'] = df.apply(lambda row: get_base64_image(f"compound_structures/compound_{row['PubChem_CID'].split('/')[-1]}.jpg"), axis=1)

citation_number = st.slider("Literature score", -2, 20, (0, 10))
df_filtered = df[df['score'].between(citation_number[0], citation_number[1]) ]


df_filtered = df_filtered[['PubChem_CID', 'name', 'link_to_image', 'score', 'References', 'link_to_compound_page' ,'class']]

# Include downoad button for the filtered data
csv = df_filtered[['name', 'PubChem_CID','score' ,'References']].to_csv(index=False, sep='\t').encode('utf-8')

st.download_button(
    label="Download data as TSV",
    data=csv,
    file_name='ototoxdb_compounds.tsv',
    mime='text/tsv',
)


st.dataframe(
    df_filtered,
    use_container_width=True,
    column_config={"PubChem_CID": st.column_config.LinkColumn("PubChem CID", 
                                                              display_text="https://pubchem.ncbi.nlm.nih.gov/compound/(.*[0-9])"), # click on PubChem CID to go to PubChem
                   "name": st.column_config.TextColumn("Compound Name", pinned=True),
                                        "link_to_image": st.column_config.ImageColumn("Structure", help="Compound structure image"),
                    "link_to_compound_page": st.column_config.LinkColumn("Details", 
                                                                      display_text=":material/open_in_new:"),}, 
    
                hide_index=True)
