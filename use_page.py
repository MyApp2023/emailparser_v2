import streamlit as st

def use_page():
    # Check and initialize session state
    if 'page' not in st.session_state:
        st.session_state.page = 'main'
    
    # Check if we should display the terms of use page
    if st.session_state.page == 'terms':
        terms_of_use_page()
        return  # Stop further execution if on terms page

    # Constants
    MAX_URLS = 50

    # Counter for generating unique widget keys
    global widget_counter
    widget_counter = 0

    def get_unique_key():
        global widget_counter
        widget_counter += 1
        return f"widget_{widget_counter}"

    def read_config_file():
        config = {}
        with open("config.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                key, value = line.strip().split("=")
                config[key] = value
        return config

    def get_place_urls(query, num_results, api_key):
        import googlemaps
        gmaps = googlemaps.Client(key=api_key)
        response = gmaps.places(query=query)
        results = []
        for place in response['results']:
            place_details = gmaps.place(place_id=place['place_id'], fields=['website'])
            if 'website' in place_details['result']:
                results.append(place_details['result']['website'])
            if len(results) == num_results:
                break
        return results[:num_results]

    def get_search_results(query, num_results, api_key, search_engine_id):
        import requests
        url = f'https://www.googleapis.com/customsearch/v1?key={api_key}&cx={search_engine_id}&q={query}'
        response = requests.get(url)
        data = response.json()
        items = data.get('items', [])
        results = [item['link'] for item in items[:num_results]]
        return results[:num_results]

    def find_email_addresses(urls, max_emails):
        import requests
        import re
        email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
        email_addresses = {}
        for i, url in enumerate(urls, start=1):
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    email_matches = re.findall(email_regex, response.text)
                    if email_matches:
                        filtered_emails = set()  # Use a set to remove duplicates
                        for email in email_matches:
                            if not email.endswith(("wixpress.com", "sentry.io", ".png", "jpg", ".html")):
                                filtered_emails.add(email)
                        if filtered_emails:
                            email_addresses[url] = list(filtered_emails)[:max_emails]  # Limit the number of emails
                        else:
                            email_addresses[url] = ['Email not found']
                    else:
                        email_addresses[url] = ['Email not found']
            except requests.exceptions.RequestException as e:
                st.write(f"Error retrieving content from {url}: {e}")
            if i == MAX_URLS:
                break
        return email_addresses

    # Read API keys and search engine ID from config.txt
    config = read_config_file()
    google_maps_api_key = config.get("GOOGLE_MAPS_API_KEY", "")
    google_search_api_key = config.get("GOOGLE_SEARCH_API_KEY", "")
    search_engine_id = config.get("SEARCH_ENGINE_ID", "")

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

    # Replace the markdown link with a button
    if st.button('Terms of Use'):
        st.session_state.page = 'terms'

    # Add a checkbox for accepting the terms of use
    accept_terms = st.checkbox('I accept the Terms of Use.')
    if not accept_terms:
        st.warning("You must accept the Terms of Use to proceed.")
        return  # Stop further execution if terms are not accepted
    
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
