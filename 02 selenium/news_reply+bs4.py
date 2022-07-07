from selenium import webdriver
import time

# 웹 자동화 TIP
# 웹 자동화 할때는 selenium을 하되
# 웹 크롤링 시에는 접근해서 소스코드 보는 것까지는 selenium으로
# 구문 분석과 데이터 추출은 selenium과 bs4를 같이 쓰는 것이 난이도와 속도면에서 좋다

def get_replys(url, imp_time=6, delay_time=0.2):  # imp_time을 너무 적게 주면 웹 페이지가 활성화
                                                # 되지 않았는데 다음 동작 실행해 에러 발생 가능
                                                # 너무 많이 주면 시간 낭비

    # 웹 드라이버
    driver = webdriver.Chrome('./chromedriver.exe')
    driver.implicitly_wait(imp_time)
    driver.get(url)

    # 더보기 끝까지 클릭하기
    while True:
        try:
            더보기 = driver.find_element_by_css_selector('a.u_cbox_btn_more')  # a태그라서 a.
            더보기.click()
            time.sleep(delay_time)
        except:
            break
    html = driver.page_source
    # print(html)

    # 모듈 참조
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, 'lxml')  # 'lxml' : html.parser보다, 속도가 제일 빠른 parser

    # 댓글 추출
    contents = soup.select('span.u_cbox_contents')
    contents = [content.text for content in contents]

    # 작성자 추출
    nicks = soup.select('span.u_cbox_nick')
    nicks = [nick.text for nick in nicks]

    # 날짜 추출
    dates = soup.select('span.u_cbox_date')
    dates = [date.text for date in dates]

    # 취합
    replys = list(zip(nicks, dates, contents))

    driver.quit()  # 전체 종료
    return replys

if __name__ == '__main__':
    from datetime import datetime
    start = datetime.now()

    # url = 'https://n.news.naver.com/article/comment/028/0002577350'
    url = 'https://n.news.naver.com/article/comment/028/0002577349'
    reply_data = get_replys(url)

    import pandas as pd
    col = ['작성자', '날짜', '내용']
    data_frame = pd.DataFrame(reply_data, columns = col)
    data_frame.to_excel('news.xlsx', sheet_name ='윤석열 조회장', startrow=0, header=True)

    end = datetime.now()
    print(end - start)