# xpath : 셀레늄에서 사용하는 특정 요소를 가리키는 경로 지정법

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('Chromedriver') # 같은 폴더 내에 있으므로 이렇게 써줄수 있다
driver.get('https://www.youtube.com/')

time.sleep(3)

# 검색어 창을 찾아 search 변수에 저장
search = driver.find_element_by_xpath('//*[@id="search"]')

search.send_keys('우왁굳')
time.sleep(1)

# search 변수에 저장된 곳에 엔터를 입력
search.send_keys(Keys.ENTER)



