# 웹 서버에 요청하고 응답받기
# 정상적인 페이지 요청시 [Response (200) 응답]
# 비정상적인 페이지 요청시 [Response (400) 응답]
import requests

url = "http://www.python.org"
resp = requests.get(url)
print(resp)

url2 = "https://www.python.org/1"
resp2 = requests.get(url2)
print(resp2)
