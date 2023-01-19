from bs4 import BeautifulSoup
import requests

URL = "https://www.imdb.com/list/ls055592025/"

response = requests.get(URL)
page = response.text
soup = BeautifulSoup(page, "html.parser")
all_movies = [tag.find(name="a").text for tag in soup.find_all(name="h3", class_="lister-item-header")]

with open("top_movies.txt","w") as file:
    for n, movie in enumerate(all_movies):
        file.write(f"{n+1}. {movie}\n")