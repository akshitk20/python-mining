import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.imdb.com/search/title/?release_date=2023-01-01,2024-07-14"
LOAD_DATA = True

if LOAD_DATA:
    response = requests.get(BASE_URL)
    print(response.status_code)
    html_doc = response.text
    with open("data/imdb.html", 'w') as file:
        file.write(html_doc)
else:
    with open("data/imdb.html") as file:
        html_doc = file.read()


soup = BeautifulSoup(html_doc,'html.parser')
print(soup)


