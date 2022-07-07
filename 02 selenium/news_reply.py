from selenium import webdriver
import time

def get_replys(url, imp_time=5, delay_time=0.2):  # imp_time을 너무 적게 주면 웹 페이지가 활성화
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
    print('끝')

    # 댓글 추출                                        # span 태그라서 span.
    contents = driver.find_elements_by_css_selector('span.u_cbox_contents')
    contents = [content.text for content in contents]

    # 작성자 추출
    nicks = driver.find_elements_by_css_selector('span.u_cbox_nick')
    nicks = [nick.text for nick in nicks]

    # 날짜 추출
    dates = driver.find_elements_by_css_selector('span.u_cbox_date')
    dates = [date.text for date in dates]
    # print(nicks,dates, contents, sep='\n')

    # 취합
    replys = list(zip(nicks, dates, contents))
    # for reply in replys:
    #     print(reply)   # 얘는 왠지 모르겠는데 print(reply for reply in replys)로 출력이 안됨.

    driver.quit()  # 전체 종료
                    # driver.close()는 그 탭만 종료
    return replys

if __name__ == '__main__':
    from datetime import datetime
    start = datetime.now()

    url = 'https://n.news.naver.com/article/comment/028/0002577350'
    reply_data = get_replys(url)

    import pandas as pd
    col = ['작성자', '날짜', '내용']
    data_frame = pd.DataFrame(reply_data, columns = col)
    data_frame.to_excel('news.xlsx', sheet_name ='포퓰리즘과 코로나 사망자 수', startrow=0, header=True)

    end = datetime.now()
    print(end - start)