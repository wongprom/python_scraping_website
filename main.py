import requests
from bs4 import BeautifulSoup


# TODO 1. Test to scrap website
# response = requests.get("https://news.ycombinator.com/news")
# yc_web_page = response.text
#
# soup = BeautifulSoup(yc_web_page, 'html.parser')
#
# articles = soup.find_all(name="span", class_="titleline")
# scores = soup.find_all(name="span", class_="score")
#
# articles_text = [article.getText() for article in articles]
# articles_link = [article.find(name="a").get("href") for article in articles]
# articles_score = [int(score.getText().split()[0]) for score in scores]
#
# highest_score = max(articles_score)
# index_highest_score = articles_score.index(highest_score)
# print(articles_text[index_highest_score])
# print(articles_link[index_highest_score])

# TODO 1. Test to scrap website and add titles to movie.txt
URL = "https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
empire_online_page = response.text
soup = BeautifulSoup(empire_online_page, 'html.parser')
all_movies = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")
movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]

with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")