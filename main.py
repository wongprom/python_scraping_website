import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')

articles = soup.find_all(name="span", class_="titleline")
scores = soup.find_all(name="span", class_="score")

articles_text = [article.getText() for article in articles]
articles_link = [article.find(name="a").get("href") for article in articles]
articles_score = [int(score.getText().split()[0]) for score in scores]

highest_score = max(articles_score)
index_highest_score = articles_score.index(highest_score)
print(articles_text[index_highest_score])
print(articles_link[index_highest_score])
