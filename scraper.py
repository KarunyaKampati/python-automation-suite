import requests
from bs4 import BeautifulSoup

def scrape():
    url = "https://example.com"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    print("Title:", soup.title.string)