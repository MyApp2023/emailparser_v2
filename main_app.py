import streamlit as st
from home_page import home_page
from use_page import use_page
from terms_of_use_page import terms_of_use_page

# Initialize session state for navigation
if 'page' not in st.session_state:
    st.session_state.page = 'home'

st.sidebar.title("Pages")
if st.sidebar.button("Home"):
    st.session_state.page = 'home'
if st.sidebar.button("Start"):
    st.session_state.page = 'use'
if st.sidebar.button("Terms of Use"):
    st.session_state.page = 'terms'

# Display the corresponding page
if st.session_state.page == 'home':
    home_page()
elif st.session_state.page == 'use':
    use_page()
elif st.session_state.page == 'terms':
    terms_of_use_page()
