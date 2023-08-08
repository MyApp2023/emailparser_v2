
import streamlit as st
from home_page import home_page
from use_page import use_page
from terms_of_use_page import terms_of_use_page

st.sidebar.title("Navigation")
if st.sidebar.button("Home"):
    home_page()
if st.sidebar.button("Use"):
    use_page()
if st.sidebar.button("Terms of Use"):
    terms_of_use_page()
