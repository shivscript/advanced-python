import requests
from bs4 import BeautifulSoup


def scrape_jobs():
    url = "https://example.com/jobs"  # demo URL
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    jobs = []
    for job in soup.find_all("div", class_="job"):
        title = job.find("h3").text
        location = job.find("span", class_="location").text
        jobs.append({"title": title, "location": location, "source": "web"})
    return jobs
