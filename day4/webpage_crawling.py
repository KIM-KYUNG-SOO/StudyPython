# Web page 긁어오기
# web page는 request에 대한 response다.
# from urllib.request import Request, urlopen

# req = Request('https://www.naver.com') # 네이버 웹페이지 요청
# res = urlopen(req)

# print(res.status) # 200 -> 웹페이지 reponse OK
                    # 404 -> 웹페이지 not found

#pip install requests
import requests
url = 'https://www.naver.com'
res = requests.get(url)

print(res.status_code)
print(res.text)
