import requests
from bs4 import BeautifulSoup


def scrape_courses():
    url = "https://books.toscrape.com/"
    response = requests.get(url, verify=False)

    soup = BeautifulSoup(response.text, "html.parser")

    courses = []

    for book in soup.select("article.product_pod"):
        title = book.h3.a["title"]
        courses.append({"course_name": title, "source": "web"})

    return courses
