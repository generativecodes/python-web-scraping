import requests

URL = '' 

site = requests.get(URL)
html = site.content
with open("website.html", "wb") as f:
    f.write(html)
