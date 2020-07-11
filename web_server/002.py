# 웹페이지에 있는 html 소스코드를 가져와서 보여준다.
import requests

url = "https://www.python.org/"
resp = requests.get(url)

html = resp.text
print(html)
