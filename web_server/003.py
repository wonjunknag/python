# 로봇 배제 표준(robots.txt)
'''
User-agent: *
Allow: /   
모든(*) 로봇(User-agent)에게 루트 디렉토리(/) 이하 모든 문서에 대한 접근을 허락(Allow)

User-agent: googlebot
Disallow: /   
특정한 로봇(googlebot)ㅇ게 모든 문서에 대한 접근을 차단(Disallow)한다.
'''
import requests

urls = ["https://www.naver.com/", "https://www.python.org/"]
filename = "robots.txt"

for url in urls:
    file_path = url + filename
    print(file_path)
    resp = requests.get(file_path)
    print(resp.text)
    print("\n")
