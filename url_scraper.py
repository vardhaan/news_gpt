from selenium import webdriver
from bs4 import BeautifulSoup

def scrape_url(url):
    driver_options = configure_driver_options()
    driver = webdriver.Chrome(chrome_options=driver_options)
    driver.get(url)
    page_source = driver.page_source
    text = scrape_text(page_source)
    return text

def configure_driver_options():
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument('--disable-javascript')
    return driver_options

def scrape_text(page_source):
    soup = BeautifulSoup(page_source, 'html.parser')
    text = soup.get_text()
    return text

