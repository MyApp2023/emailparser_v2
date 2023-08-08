
import streamlit as st
from home_page import home_page
from use_page import use_page
from terms_of_use_page import terms_of_use_page

st.sidebar.title("Navigation")
page = st.sidebar.success("Go to", ["Home", "Use", "Terms of Use"])

if page == "Home":
    home_page()
elif page == "Use":
    use_page()
elif page == "Terms of Use":
    terms_of_use_page()
