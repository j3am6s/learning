import requests
from bs4 import BeautifulSoup
import os

URL = "https://www.billboard.com/charts/hot-100/"

date = input("When do you want to travel to? (YYYY-MM-DD) ")

response = requests.get(f"{URL}{date}/")
soup = BeautifulSoup(response.text, "html.parser")

songs = [song.getText().strip() for song in soup.select("li ul li h3")]


import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = os.environ.get("client_id")
CLIENT_SECRET = os.environ.get("client_secret")
redirect = "http://example.com"

spotify_auth = spotipy.oauth2.SpotifyOAuth(client_id=CLIENT_ID,
                                           client_secret=CLIENT_SECRET,
                                           redirect_uri=redirect,
                                           scope="playlist-modify-private",
                                           cache_path="scraping/token.txt")


sp = spotipy.Spotify(oauth_manager=spotify_auth)

user_name = sp.current_user()["display_name"]
user_id = sp.current_user()["id"]

song_urls = []
for song in songs:
    items = sp.search(q=f"track: {song} year: {date[:4]}", type="track")["tracks"]["items"]
    if len(items) > 0:
        song_urls.append(items[0]["uri"])

playlist_id = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)["id"]

sp.playlist_add_items(playlist_id=playlist_id, items=song_urls)
