from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

soup = BeautifulSoup(response.text, "html.parser")

#makes a title with all the movies
titles = [title.string for title in soup.find_all(name="h3", class_="title")]

#adds every movie, in order, to a "100movies.txt" file
with open("scraping/100movies.txt", "w") as file:
    for title in titles[::-1]:
        file.write(title)
        file.write("\n")
