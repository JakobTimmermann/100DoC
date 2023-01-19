from bs4 import BeautifulSoup
import requests
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

authManager = SpotifyOAuth(
    scope="playlist-modify-private",
    client_id=os.environ["SPOTIPY_CLIENT_ID"],
    client_secret=os.environ["SPOTIPY_CLIENT_SECRET"],
    redirect_uri="http://example.com",
    show_dialog=True,
    cache_path="token.txt"
    )
sp = spotipy.Spotify(auth_manager=authManager)
user_id = sp.current_user()["id"]
date = input("Which year do you want to travel? Format: YYYY-MM-DD:  ")
if date == "":
    date = "2005-05-30"
BASE_URL = "https://www.billboard.com/charts/hot-100/"
playlist= sp.user_playlist_create(user=user_id, name=f"Billboard Top100 from {date}", public=False)

response = requests.get(BASE_URL + date)
page = response.text
soup = BeautifulSoup(page, "html.parser")
song_tags = [tag.find_all(name="h3", class_="c-title") for tag in soup.find_all(name="li", class_="lrv-u-width-100p")]
artist_tags = [tag.find_all(name="span", class_="a-no-trucate") for tag in soup.find_all(name="li", class_="o-chart-results-list__item")]
songs = [l[0].text.strip() for l in song_tags if len(l) > 0]
artists = [l[0].text.strip() for l in artist_tags if len(l) > 0]

song_uris = []
year = date.split("-")[0]
for song in songs:
    result = sp.search(q=f"track:{song} year:{year}", type='track')
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} does't exist in Spotify. Skipped.")

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

