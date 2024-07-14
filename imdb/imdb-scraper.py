import requests
from bs4 import BeautifulSoup
from pprint import pprint

BASE_URL = "https://www.imdb.com/search/title/?release_date=2023-01-01,2024-07-14"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}
LOAD_DATA = False

if LOAD_DATA:
    response = requests.get(BASE_URL, headers=headers)
    print(response.status_code)
    html_doc = response.text
    with open("data/imdb.html", 'w') as file:
        file.write(html_doc)
else:
    with open("data/imdb.html") as file:
        html_doc = file.read()

soup = BeautifulSoup(html_doc, 'html.parser')
#print(soup.prettify())

movies = soup.find_all("div", class_='ipc-page-grid__item ipc-page-grid__item--span-2')
#print(movies)
count = 0
for movie in movies:
    #print(movie)
    count = count + 1
    name = movie.find_all('a', class_='ipc-title-link-wrapper')
    pprint(name)
    print(name[3:])
    year = movie.find_all('span', class_='sc-b189961a-8 kLaxqf dli-title-metadata-item')
    pprint(year)
    rating = movie.find_all('span', {"aria-label": lambda x: x and x.startswith("IMDb rating:")})
    # rating = rating['aria-label'].split(":")[1].strip()
    pprint(rating)

print(count)