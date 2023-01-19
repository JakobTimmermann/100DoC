from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
page = response.text

soup = BeautifulSoup(page, "html.parser")

idx = [tag.attrs["id"] for tag in soup.find_all(name="tr", class_="athing")]

article_info = {}
for id in idx[:100]:
    print(id)
    article_tag = soup.find(id=id).find(class_="titleline").find(name="a")
    title = article_tag.text
    try:
        upvotes = int(soup.find(id=f"score_{id}").text.split()[0])
        article_info[title] = [upvotes, article_tag.get("href")]
    except AttributeError:
        print(soup.find(id=f"score_{id}"))

sorted_articles = dict(sorted(article_info.items(), key=lambda x:x[1], reverse=True))
print(sorted_articles)

