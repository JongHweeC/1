from bs4 import BeautifulSoup
from pprint import pprint
import requests

# 웹 페이지를 열고 소스코드를 읽어오는 작업
html = requests.get("http://comic.naver.com/webtoon/weekday")
soup = BeautifulSoup(html.text, 'html.parser')
html.close()  # 적어주면 좋음
'''
# 월요웹툰영역 추출하기
data1 = soup.find('div',{'class':'col_inner'})
pprint(data1)

# 제목 포함영역 추출하기
data2 = data1.findAll('a',{'class':'title'})
pprint(data2)

# 텍스트만 추출
title_list = [t.text for t in data2]
print(title_list)

## 요약 1. 월요 웹툰영역 find, 2. 해당 영역 제목,  findAll 3. for로 text 추출
'''
# 모든 요일 웹툰 제목 추출
data1_list = soup.findAll('div',{'class':'col_inner'})
# pprint(data1_list)

week_title_list = []
# 제목 포함영역 추출하기
for data1 in data1_list:
    data2 = data1.findAll('a',{'class':'title'})
    title_list = [t.text for t in data2]
    week_title_list.append(title_list)  # 이중리스트
    #week_title_list.extend(title_list)  리스트 1개에 이어서
pprint(week_title_list)
print(week_title_list[0][0])