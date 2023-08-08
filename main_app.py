import streamlit as st
from home_page import home_page
from use_page import use_page
from terms_of_use_page import terms_of_use_page

# Create navigation links
st.sidebar.title("Navigation")
st.sidebar.markdown("[Home](?page=home)")
st.sidebar.markdown("[Use](?page=use)")
st.sidebar.markdown("[Terms of Use](?page=terms)")

# Get the page from the query parameter
page = st.experimental_get_query_params().get("page", [None])[0]

# Display the corresponding page
if page == "home":
    home_page()
elif page == "use":
    use_page()
elif page == "terms":
    terms_of_use_page()
else:
    # Default page (e.g., home page)
    home_page()
