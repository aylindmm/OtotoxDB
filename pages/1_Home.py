import streamlit as st
# Show the page title and description.
st.set_page_config(page_title="OtotoxDB", page_icon="🥗")
st.title("Otoactive Compounds Data Base")
st.write(
    """
    Welcome to the OtotoxDB, a comprehensive database of compounds that have been shown to have ototoxic effects.
    This database is designed to provide researchers, clinicians, and students with easy access to information about ototoxic compounds, including their chemical properties, mechanisms of action, and associated research articles.
    
    The database was built using Large Language Models (LLMs) to extract and organize data from scientific literature, ensuring that the information is up-to-date and accurate. We hope that OtotoxDB will serve as a valuable resource for those studying ototoxicity and related fields.
    """
)