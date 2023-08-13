import streamlit as st

def home_page():
    st.title("Welcome to FindMail")
    
    st.write(
        "How many times have you tried to email multiple people with the same request "
        "to get the best reply, opinion, or proposition? If you only message one employee, "
        "customer, lawyer, electrician, contractor, or investor, you're missing out. One shot \n\n"
        
        "Find the best fit for your task or simply pose a question to multiple people and "
        "compare their answers or quotes with our tool.\n\n"
        
        "To contact someone, you need an email. But how long does it take you to find an email "
        "on a website? Probably a minute or two. And for several websites? Roughly 5 minutes. "
        "But what if you need to search through 5, 10, 20, 30, or 50 websites? We'll handle the "
        "manual process for you: searching for websites, keeping track of which ones you've visited, "
        "and sifting through pages to find contact information.\n\n"
        
        "Our bot will assist you in searching either general Google results or the business section "
        "through any reasonable number of websites to retrieve emails instantly. Just type in a search "
        "query, specify the number of websites, review them, and obtain emails.\n\n"
        
        "Save your time; let the code handle the manual work for you!"
    )
    
    if st.button("Try for Free"):
        st.session_state.page = 'use'
