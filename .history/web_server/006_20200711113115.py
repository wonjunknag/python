import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway"
resp = requests.get(url)
html_src = resp.text

soup = BeautifulSoup(html_src, "html.parser")

target_img = soup.find(
    name="img", attrs={"alt": "Seoul-Metro-2004-20070722.jpg"})
print("HTML 요소", target_img)
print("\n")

target_img_src = target_img.get("src")
print("이미지 파일 경로: ", target_img_src)
print("\n")
