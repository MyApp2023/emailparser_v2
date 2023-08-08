
import streamlit as st

def home_page():
    st.title("Welcome to My App")
    st.write("This is the home page of the application. You can navigate to other pages from here:")

    if st.button("Go to Use Page"):
        st.session_state.page = 'use'

    if st.button("Go to Terms of Use Page"):
        st.session_state.page = 'terms'
