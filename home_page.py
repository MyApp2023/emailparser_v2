
import streamlit as st

def home_page():
    st.title("Welcome to My App")
    st.write("This is the home page of the application. You can navigate to other pages from here:")

    st.markdown("[Try it now](?page=use)")

