import pandas as pd
import requests
from bs4 import BeautifulSoup
import time

# 기존 CSV 파일 로드
file_path=""
df = pd.read_csv("festival_data2.csv")

# 'info' 컬럼 추가
df['info'] = None



# 각 URL에 대해 추가 정보 크롤링
for index, row in df.iterrows():
    url = row['detail_link']

    # URL이 비어있을 경우 건너뛰기
    if pd.isna(url):
        continue

    # URL 접속
    response = requests.get(url)


    if response.status_code != 200:
        print(f"Failed to retrieve data from {url}")
        continue

    # BeautifulSoup 파싱
    soup = BeautifulSoup(response.text, 'html.parser')


    # 추가 정보 크롤링 (selector #rmjs-1 내 <a> 태그 내용)
    info = soup.select_one("p.add_intro")

    if info:
        # print('index',index)
        info_text = info.text.strip()
        df.at[index, 'info'] = info_text
    else:
        df.at[index, 'info'] = None


'''
    # 서버에 부담을 줄이기 위해 대기
    time.sleep(1)


'''

# 새로운 CSV 파일로 저장
df.to_csv("festival_data_with_info3.csv", index=False, encoding="utf-8")

print("Data with additional information saved to festival_data_with_info.csv")

