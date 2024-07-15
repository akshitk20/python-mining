import requests
from bs4 import BeautifulSoup
from pprint import pprint
import csv

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

movies = soup.find_all("ul", class_='ipc-metadata-list ipc-metadata-list--dividers-between sc-748571c8-0 jmWPOZ detailed-list-view ipc-metadata-list--base')
movies_csv = []
count = 0
names = soup.find_all('a', class_='ipc-title-link-wrapper')
print(type(movies))
name_csv = []
year_csv = []
rating_csv = []
for name in names:
    name_csv.append(name.string[3:].strip())
years = soup.find_all('span', class_='sc-b189961a-8 kLaxqf dli-title-metadata-item')
for year in years:
    year_csv.append(year.string)
ratings = soup.find_all('span', {"aria-label": lambda x: x and x.startswith("IMDb rating:")})
for rating in ratings:
    rating_csv.append(rating['aria-label'].split(":")[1].strip())
print(len(name_csv))
print(year_csv)
print(rating_csv)
year_csv_grouped = [year_csv[i:i + 3] for i in range(0, len(year_csv), 3)]
print(len(year_csv_grouped))
for i, name in enumerate(name_csv):
    if i == 20:
        break
    movie_name = name_csv[i]
    movie_rating = rating_csv[i]
    year_rating = year_csv_grouped[i]
    movie_csv = {
        "Name": movie_name,
        "Rating": movie_rating,
        "Year": year_rating[0],
        "Duration": year_rating[1],
        "Certificate": year_rating[2]
    }
    movies_csv.append(movie_csv)
pprint(movies_csv)

with open("data/movies.csv",'w') as file:
    writer = csv.DictWriter(file, fieldnames=('Name','Rating','Year','Duration','Certificate'))
    writer.writeheader()
    writer.writerows(movies_csv)

#pprint(movies_csv)
#print(count)
