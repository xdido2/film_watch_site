# https://www.pycodemates.com/2022/02/scrape-movie-information-from-imdb-using-python-and-bs4.html

import requests
from bs4 import BeautifulSoup
import pandas as pd

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "DNT": "1",
    "Connection": "close", "Upgrade-Insecure-Requests": "1"}

genres = [

    "Adventure",
    "Animation",
    "Biography",
    "Comedy",
    "Crime",
    "Drama",
    "Family",
    "Fantasy",
    "Film-Noir",
    "History",
    "Horror",
    "Music",
    "Musical",
    "Mystery",
    "Romance",
    "Sci-Fi",
    "Sport",
    "Thriller",
    "War",
    "Western"
]

url_dict = {}
counts = []
c = 0

for genre in genres:
    url = "https://www.imdb.com/search/title/?genres={}&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=5aab685f-35eb-40f3-95f7-c53f09d542c3&pf_rd_r=N97GEQS6R7J9EV7V770D&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_16"
    formatted_url = url.format(genre)
    url_dict[genre] = formatted_url
print(url_dict)
for i in list(url_dict.values()):
    url = i

    # Sending a request to the speciifed URL
    resp = requests.get(url, headers=HEADERS)

    # Converting the response to Beautiful Soup Object
    content = BeautifulSoup(resp.content, 'lxml')

    # Iterating throught the list of movies
    for movie in content.select('.lister-item-content'):

        try:
            # Creating a python dictonary
            data = {
                'imdb_id': movie.select('.lister-item-header > a')[0].attrs['href'].split('/')[2],
                "title": movie.select('.lister-item-header')[0].get_text().strip(),
                "year": movie.select('.lister-item-year')[0].get_text().strip(),
                "time": movie.select('.runtime')[0].get_text().strip(),
                "simple_desc": movie.select('.text-muted')[2].get_text().strip(),

            }
        except IndexError:
            continue
        c += 1
        # counts.append(len(data))
        print(c)

# print(sum(counts))
