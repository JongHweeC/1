from selenium import webdriver
from pprint import pprint
import time
from collections import Counter


driver = webdriver.Chrome('chromedriver')
driver.get('http://zzzscore.com/color/')
driver.implicitly_wait(100)  # time.sleep과 같은 역할

btns = driver.find_elements_by_xpath('//*[@id="grid"]/div')
                                      # 형식이 통일되어있지 않기에 [*]를 못 씀
                                    # bs의 findAll처럼 리스트로 반환해줌
                                    # 셀레늄의 장점 : 셀레늄으로 가져온 요소는
                                    # 실시간으로 값이 바뀌는 것을 감지
                                    # 크롬 드라이버와 연결되어 계속 최신화

def analysis():  # 색 비교로 유일한 색(다른 색)을 찾아 버튼 클릭하는 함수
    # 색정보 css property
    btns_rgba = [btn.value_of_css_property('background-color') for btn in btns]
    pprint(btns_rgba)

    result = Counter(btns_rgba)   # 딕셔너리 형태로 반환
    pprint(result) #여기서 value가 1인게 정답

    #value가 1인 것 탐색
    for key, value in result.items():
        if value == 1:
            answer = key
            break
    else:
        answer = None
        print("정답을 찾을 수 없습니다.")

    # 정답 클릭
    # 1. btns_rgba에서 인덱스 값을 구하고
    # 2. 그 인덱스 값으로 btns 인덱스에 접근. 클릭
    if answer:
        index = btns_rgba.index(answer)
        btns[index].click()
'''
start = time.time()
while time.time()-start <= 60:
    analysis()
'''
# 색 비교가 아닌 소스코드에서 정답 찾기
start = time.time()
while time.time() - start <= 60:
    try:
        btn = driver.find_element_by_class_name("main")
        btn.click()
    except:
        pass
