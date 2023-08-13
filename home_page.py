import streamlit as st

def home_page():
    st.title("Welcome to FindMail")
    
    st.write(
        
        "Find the best fit for your task or simply pose a question to multiple people and "
        "compare their answers or quotes with our tool.\n\n"

        "We'll handle the "
        "manual process for you: searching for websites, keeping track of which ones you've visited, "
        "and sifting through pages to find contact information using either general Google results or the Location-based Business Section "
        "through any reasonable number of websites to retrieve emails instantly. Just type in a search "
        "query, specify number of websites and e-mails to be extracted from a website and press search button \n\n"
        
        "Save your time; let the code handle the manual work for you!"
    )
    
    if st.button("Try for Free"):
        st.session_state.page = 'use'

    if st.button("Read Terms of Use"):
        st.session_state.page = 'terms'
