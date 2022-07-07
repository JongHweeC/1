#//*[@id="root"]/div/div[2]/div[1]/main/div[2]/div[3]/div/div/div[2]/div/div[2]/div/div/video
from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument('headless')
                # 동적 페이지(트위치)와 정적 페이지
                # headless 사용시 사용자가 어떤식으로 접근하는지 몰라 기본값으로 크롤링
                # 이 경우 날짜가 한국어가 아닌 영어로 출력됨
options.add_argument('window-size=1920x1080')
# options.add_argument("disable-gpu")
# options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")

driver = webdriver.Chrome('chromedriver', chrome_options=options)
driver = webdriver.Chrome('chromedriver')
driver.get("https://www.twitch.tv/soorte214/clip/AgileGracefulCheesecakePeteZarollTie") #특정 클립 링크

time.sleep(2)

#video 태그 확인
url_element = driver.find_element_by_tag_name('video')
vid_url = url_element.get_attribute('src')
print(vid_url)

#클립 제목과 날짜 확인
title_element1 = driver.find_element_by_class_name('tw-flex')
title_element2 = title_element1.find_elements_by_tag_name('span')
vid_title, vid_date = None, None
for span in title_element2:
    try:
        d_type = span.get_attribute('data-test-selector')
        if d_type == "title":
            vid_title = span.text
        elif d_type == 'date':
            vid_date = span.text
    except:
        pass

print(vid_title,'\t',vid_date)

#특수문자 없애고 빈칸도 없에기
# re.sub('바꾸고 싶은 문자', '바꿀 문자', '문자열이름', '바꿀 횟수')
                                # 바꿀 횟수 미지정시 모든 경우에 대해 바꿈
import re
vid_title = re.sub('[^0-9a-zA-Zㄱ-힗]', '', vid_title)
vid_date = re.sub('[^0-9a-zA-Zㄱ-힗]', '', vid_date)
print(vid_title,'\t',vid_date)

from urllib.request import urlretrieve
urlretrieve(vid_url, vid_title + '_' + vid_date + '.mp4') # 링크, 제목 + 확장자

driver.close()
