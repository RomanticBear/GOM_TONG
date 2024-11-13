import requests
from bs4 import BeautifulSoup
import pandas as pd
import re


def refine_text(text):
    # 불필요한 공백 및 특수 문자 제거
    fixed_text = re.sub(r'\r', ' ', text).replace(' ', '')
    return fixed_text


# 크롤링할 base URL
base_url = "https://xn--ok0b236bp0a.com/festival?code=all&month={}"

# 크롤링한 데이터를 저장할 리스트
data = []


# 1월부터 12월까지 데이터를 크롤링
for month in range(1, 13):
    # 해당 월의 URL 생성
    url = base_url.format(month)
    response = requests.get(url)

    # 요청 성공 여부 확인
    if response.status_code != 200:
        print(f"Failed to retrieve data for month {month}")
        continue

    # BeautifulSoup을 사용하여 HTML 파싱
    soup = BeautifulSoup(response.text, 'html.parser')

    # 각 축제 정보를 가져오기 위한 선택자 설정
    festivals = soup.select("#page > div.page-content.header-clear-medium > div.content > div > div:nth-child(4) > div")

    for festival in festivals:
        # 상세 페이지 링크
        detail_link = festival.select_one("a")["href"] if festival.select_one("a") else None
        # 축제 이름
        name = festival.select_one("a > div > div > h5").text.strip() if festival.select_one(
            "a > div > div > h5") else None
        # 축제 일자
        date = festival.select_one("a > div > div > p.card-text.mb-0 > small").text.strip().replace('\n', '').replace('\t', '').replace('~', ' ~ ').replace('\r','') if festival.select_one(
            "a > div > div > p.card-text.mb-0 > small") else None

        # 축제 위치
        location = festival.select_one("a > div > div > p.ing_card_desc.mb-0").text.strip() if festival.select_one(
            "a > div > div > p.ing_card_desc.mb-0") else None

        # 데이터 리스트에 추가
        data.append({
            # "month": month,
            "detail_link": "https://xn--ok0b236bp0a.com"+detail_link,
            "name": name,
            "date": date,
            "location": location
        })
    #
    # # 크롤링 간 서버에 부담을 주지 않도록 대기
    # time.sleep(1)

# DataFrame으로 변환
df = pd.DataFrame(data)

# CSV 파일로 저장
df.to_csv("festival_data2.csv", index=False, encoding="utf-8")

print("Data saved to festival_data.csv")