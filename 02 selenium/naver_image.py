from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from tqdm import tqdm   # 파이썬 진행률 프로세스바
                        # 간단하게는 tqdm(iterable)로 사용

def get_images(keyword):

    # 웹 접속 - 네이버 이미지 접속
    print('접속 중...')
    driver = webdriver.Chrome('./chromedriver.exe')
    driver.implicitly_wait(30)

    url = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query={}'.format(keyword)
    driver.get(url)

    # 페이지 스크롤 다운
    body = driver.find_element_by_css_selector('body')
    for i in range(3):
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(1) # 텀을 두어야 사진이 로딩되면서 더 많은 사진 다운 가능

    # 이미지 링크 수집
    imgs =driver.find_elements_by_css_selector('img._image._listImage') # 태그명 + 클래스명 접근시 (.) + _img(=클래스명)
    result = []
    for img in tqdm(imgs):
        if 'http' in img.get_attribute('src'):
            result.append(img.get_attribute('src'))
    print(result)

    driver.close()
    print('수집 완료!')

    # 폴더 생성
    print('폴더 생성!')
    import os

    if not os.path.isdir('./{}'.format(keyword)):
        os.mkdir('./{}'.format(keyword)) # 현재 주소에 폴더 생성

    # 폴더에 다운로드
    print('다운로드 중...')
    from urllib.request import urlretrieve

    for index, link in tqdm(enumerate(result)):  # enumerate(iterable) : index, value 2개값을 반환
        # 파일형식 확인(jpg, jpeg, png..)
        start = link.rfind('.')  # rfind는 뒤에서부터 탐색
        end = link.rfind('&')
        filetype = link[start:end]  # 가끔씩 이 형식이 안맞아서 사진으로 저장되지 않는 애들도 있음

        urlretrieve(link, './{}/{}{}{}'.format(keyword, keyword, index, filetype))
        time.sleep(0.1) # 다운로드에 딜레이를 두어
    print('다운로드 완료!')

    # 압축 - 메일
    import zipfile
    zip_file = zipfile.ZipFile('./{}.zip'.format(keyword), 'w')

    print(os.listdir('./{}'.format(keyword)))
    for image in tqdm(os.listdir('./{}'.format(keyword))):  #  폴더 안의 파일명을 가져오는 코드
                                                        # 키워드 폴더안의 사진을 리스트로
                                                        # 여기서 image변수는 사진파일명
        zip_file.write('./{}/{}'.format(keyword, image), compress_type=zipfile.ZIP_DEFLATED)
    zip_file.close()
    print('압축 완료!')

if __name__ == '__main__':
    keyword = input('수집할 이미지 키워드를 입력하세요 : ')
    get_images(keyword)