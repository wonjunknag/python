import requests

url = "https://www.ython.org/"
resp = requests.get(url)

html = resp.text
print(html)
