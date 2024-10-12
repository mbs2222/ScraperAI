from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

def scrape_website_text(url):
    # Set up Chrome options for headless browsing
    chrome_options = webdriver.ChromeOptions()
    chrome_driver_path = "./chromedriver.exe"
    # Initialize the WebDriver
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)

    try:
        # Navigate to the URL
        driver.get(url)

        # Get the page source
        page_source = driver.page_source



        return page_source

    finally:
        # Close the browser
        driver.quit()

def extract_text_from_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    body_content = soup.body
    if body_content:
        return str(body_content)   
    return ""


def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, 'html.parser')

    for script in soup(["script", "style"]):
        script.extract()

    clean_text = soup.get_text(separator="\n")
    clean_text = "\n".join(
        line.strip() for line in clean_text.splitlines() if line.strip()
        )
    return clean_text

def split_dom_content(dom_content, max_length=6000):
    return [
        dom_content[i:i+max_length] for i in range(0, len(dom_content), max_length)
        ]
