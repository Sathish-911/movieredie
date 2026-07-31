import requests
from bs4 import BeautifulSoup
import json

URL = "https://www.5movierulz.vote/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

data = []

for a in soup.find_all("a", href=True):
    title = a.get_text(strip=True)
    href = a["href"]

    if title:
        data.append({
            "title": title,
            "url": href
        })

with open("urls.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)