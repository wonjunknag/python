# beautifulsoup 프레임워크를 통해서 request로 요청한 내용을
# html.parser을 통해 html태그에 원하는 내용을 분류할 수 있다.
import requests
from bs4 import BeautifulSoup

url = "https://ko.wikipedia.org/wiki/Seoul_Metropolitan_Subway"
resp = requests.get(url)
html_src = resp.text
# print(html_src)

soup = BeautifulSoup(html_src, 'html.parser')
print(type(soup))
print("\n")

print(soup.head)
print("\n")
print(soup.body)
print("\n")

print("title 태그 요소: ", soup.title)
print("title 태그 이름: ", soup.title.name)
print("title 태그 문자열: ", soup.title.string)
