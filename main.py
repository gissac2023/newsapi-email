import requests
import os
from send_email import send_email

api_key = os.getenv("api_key")
url = f"https://newsapi.org/v2/everything?q=tesla&from=2023-04-" \
      f"24&sortBy=publishedAt&apiKey={api_key}"

request = requests.get(url)
content = request.json()
# print(type(content))
# print(content['articles'])
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
send_email(body)
