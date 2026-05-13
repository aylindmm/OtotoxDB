import streamlit as st
import pandas as pd
# Add a home page (your current main script)
main_page = st.Page("pages/1_Home.py", title="Home", default=True)

# Define your pages
# The 'title' is what shows in the sidebar, 'icon' is optional
compounds_page = st.Page("pages/2_Compounds.py", title="Compounds")
articles_page = st.Page("pages/3_Articles.py", title="Articles")
download_page = st.Page("pages/4_Download.py", title="Download")


# Sidebar navigation (matches the left panel in your image)
with st.sidebar:
    st.page_link(main_page, label="Home", icon="🏠")
    st.page_link(compounds_page, label="Compounds")
    st.page_link(articles_page, label="Articles")
    st.page_link(download_page, label="Download")

df = pd.read_csv("data/compounds.tsv", sep="\t")

df = df.sort_values(by="name")

# 1. Create the list of pages
compound_pages = []
for index, row in df.iterrows():
    cid = row['PubChem_CID']
    name = row['name']
    # Ensure these .py files actually exist in your 'compounds' folder!
    page = st.Page(f"compound_pages/compound_{cid}.py", title=f"{name}")
    compound_pages.append(page)

# 2. Define your main app structure
# You must include the compound_pages list here
pg = st.navigation({
    "Main Menu": [
        st.Page("pages/1_Home.py", title="Home", icon="🏠"),
        st.Page("pages/2_Compounds.py", title="Compounds"),
        st.Page("pages/3_Articles.py", title="Articles"),
        st.Page("pages/4_Download.py", title="Download")
        
    ],
    "Compounds": compound_pages  # This adds them to the nav bar
}, position="top")

pg.run()

