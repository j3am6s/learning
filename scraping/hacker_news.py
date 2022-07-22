from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

#make list of all articles, links and upvotes
articles = soup.find_all(name="a", class_="titlelink")
article_text = [article.getText() for article in articles]
article_link = [article.get("href") for article in articles]
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

#print article and link that have the largest number of upvotes
index = article_upvotes.index(max(article_upvotes))
print(article_text[index])
print(article_link[index])

