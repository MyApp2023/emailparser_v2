
import streamlit as st
st.title("Email Parser")

# Prompt for search input
search_query_key = get_unique_key()
search_query = st.text_input("Enter the search string:", key=search_query_key)

api_choice_key = get_unique_key()
api_choice = st.selectbox(
    "Select to use Google Businesses or Google Search:",
    ('Google Businesses', 'Google Search'),
    key=api_choice_key
    )
num_results_key = get_unique_key()
num_results = st.number_input("How many URLs do you want to get?", min_value=1, max_value=MAX_URLS, step=1, value=1, key=num_results_key)

max_emails_key = get_unique_key()
max_emails = st.number_input("Maximum number of emails to extract from each URL:", min_value=1, max_value=100, step=1, value=2, key=max_emails_key)

    # Search and extract e-mails button
search_emails_button_key = get_unique_key()
search_emails = st.button("Search and extract e-mails", key=search_emails_button_key)

if search_query and api_choice and num_results and search_emails:
    if api_choice == 'Google Businesses' and google_maps_api_key:
        st.info("Fetching URLs and e-mails using Google Places API...")
        urls = get_place_urls(search_query, num_results, google_maps_api_key)
        email_addresses = find_email_addresses(urls, max_emails)
        for i, (url, email_list) in enumerate(email_addresses.items(), start=1):
            st.write(f"\n{i}. {url}\n")
            for email in email_list:
                st.write(f"- {email}")
    elif api_choice == 'Google Search' and google_search_api_key and search_engine_id:
        st.info("Fetching URLs and e-mails using Google Custom Search API...")
        urls = get_search_results(search_query, num_results, google_search_api_key, search_engine_id)
        email_addresses = find_email_addresses(urls, max_emails)
        for i, (url, email_list) in enumerate(email_addresses.items(), start=1):
            st.write(f"\n{i}. {url}\n")
            for email in email_list:
                st.write(f"- {email}")
    else:
        st.error("Missing API key or search engine ID. Please check the configuration.")

# Reset widget keys to avoid duplicate key issue when rerunning the app
widget_counter = 0

    # You can add your main function or logic here to be executed on the "Use" page
