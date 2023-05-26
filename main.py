import requests
import os
from send_email import send_email

api_key = os.getenv("api_key")
topic = "japan"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}" \
      "&from=2023-04-26" \
      "&sortBy=publishedAt" \
      f"&apiKey={api_key}" \
      "&language=en"

request = requests.get(url)
content = request.json()
# print(type(content))
# print(content['articles'])
body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = "Subject: Today's news" + "\n" \
               + body + article["title"] \
               + "\n" + article["description"] \
               + "\n" + article["url"] + 2 * "\n"

body = body.encode("utf-8")
send_email(body)
