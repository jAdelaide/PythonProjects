import requests
from bs4 import BeautifulSoup

print()
When = input("What month do you want to seach for?  (yy-mm)\t")
r = requests.get('https://www.imdb.com/movies-coming-soon/20' + str(When) + '/?ref_=cs_dt_nx')

soup = BeautifulSoup(r.text, 'html.parser')

print()

movies = []

for item in soup.find_all('h4'):
    if ' (20' in str(item.string):
     Movie = str(item.string).split('(')
     movie_dict = {}
            # Title is bit before ' ('
     Title = (Movie[0])
     print(str(Title))
     print("    -----")
     

