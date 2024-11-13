import requests
from bs4 import BeautifulSoup

response=requests.get("https://startcoding.pythonanywhere.com/basic") # 응답 신호 저장할 객체 response
html=response.text
soup=BeautifulSoup(html,'html.parser') # 문자열 형태의 html을 html.paser가 태그 객체로 하나씩 나눠서 soup에 담음

items=soup.select(".product") # 하나가 아닌 전부 가져옴 -> 리스트 형태

for item in items:
    category=item.select_one(".product-category").text # select_one: 매칭되는 태그들 중 첫번째 가져옴
    name=item.select_one(".product-name").text
    link=item.select_one(".product-name > a").attrs['href']
    price=item.select_one(".product-price").text.strip().split('원')[0].replace(',',"") # 앞뒤 공백 제거 strip
    print(category,name,link,price)
