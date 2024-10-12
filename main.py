import streamlit as st
from scrape import scrape_website_text, extract_text_from_html, clean_body_content, split_dom_content
from parse import parse_with_ollama
def main():
    st.title("AI Web Scraper")
    
    # Create an input text field
    url = st.text_input("Enter your URL here:")
    
    # Display the user input
    if st.button("Scrape Site"):
        st.write("Scraping site...")
        result = scrape_website_text(url)
        html_text = extract_text_from_html(result)
        clean_text = clean_body_content(html_text)

        st.session_state.dom_content = clean_text

        with st.expander("Show Cleaned Text"):
            st.text_area("DOM CONETENT", clean_text, height=300)

    if "dom_content" in st.session_state:
        parse_description = st.text_area("Describe what you want to parse")

        if st.button("Parse Content"):
            if parse_description:
                st.write("Parsing the content...")
                dom_chunks = split_dom_content(st.session_state.dom_content)
                parsed_result = parse_with_ollama(dom_chunks, parse_description)
                st.write(parsed_result)

if __name__ == "__main__":
    main()
