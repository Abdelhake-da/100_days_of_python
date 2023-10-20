import requests
import urllib.request
from bs4 import BeautifulSoup

URL = 'https://www.imdb.com/chart/top/'
URL2 = 'https://www.imdb.com/list/ls565690655/?sort=user_rating,desc&st_dt=&mode=detail&page=1'
url = 'https://emojipedia.org/htc/sense-7/star/'
response = requests.get(URL2)
website_html = response.text
# print(website_html)
soup = BeautifulSoup(website_html, 'html.parser')

all_movies = soup.select(selector='.lister-item-header a')
# print([movie.text for movie in all_movies])
years_of_movies = soup.select(selector='.lister-item-header .lister-item-year')
# print([movie.text for movie in years_of_movies])

for movie, i, year in zip(all_movies, range(len(all_movies)), years_of_movies):
    print(f'{i+1}- {movie.text} {year.text}')
