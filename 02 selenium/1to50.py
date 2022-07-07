from selenium import webdriver

driver = webdriver.Chrome('chromedriver')
driver.get('http://zzzscore.com/1to50')
driver.implicitly_wait(300)  # time.sleep과 같은 역할

# btns = driver.find_elements_by_xpath('//*[@id="grid"]/div[*]')
                                    # bs의 findAll처럼 리스트로 반환해줌
# print(len(btns))
# print(btns[0].text) #0번 요소의 텍스트

def clickBtn(n):
    btns = driver.find_elements_by_xpath('//*[@id="grid"]/div[*]')
    for btn in btns:
        print(btn.text, end='\t')
        if btn.text == str(n):
            btn.click()
            print(True)
            return

for i in range(1,51):
    clickBtn(i)