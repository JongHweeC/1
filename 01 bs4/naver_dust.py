from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

html = requests.get('https://search.naver.com/search.naver?query=날씨')
# pprint(html.text)

soup = bs(html.text,'html.parser')
                                        # 영역 추출 - 여럿인 경우 최초를 반환
data1 = soup.find('div',{'class':'list_box'}) # (태그명, 속성값) 속성값은 딕셔너리로
pprint(data1)                         # 속성값이 찾는데 도움안될 때, tag만 넘기기도 함

data2 = data1.findAll('li')
pprint(data2)

find_dust = data2[0].find('span', {'class':'num'}).text  # text만 반환
print(find_dust)






