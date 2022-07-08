import os
import shutil
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import Select

''' selenium 4.2.0 이하에서 '''

def rename(f_path, f_name):
    """
    가장 최근에 다운 받은 파일의 이름을 바꿔준다.
    :param f_path: 파일이 저장되는 경로
    :param f_name: 새로운 파일이름
    :return:
    """
    filename = max([f_path + '\\' + f for f in os.listdir(f_path)], key=os.path.getctime)
    shutil.move(os.path.join(f_path, filename), f_name)


driver = webdriver.Chrome('chromedriver')
driver.get("https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/county/mapping/13/tavg/201705/1/value")
time.sleep(3)

states = ['Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Michigan', 'Minnesota', 'Missouri', 'Nebraska', 'North Dakota', 'Ohio', 'South Dakota', 'Wisconsin']
parameters = ['Average Temperature', 'Maximum Temperature', 'Minimum Temperature', 'Precipitation']
years = ['2017', '2018', '2019', '2020', '2021']
months = ['March', 'April', 'May', 'June', 'July', 'August', 'September']
time_scale = '1-Month'  # default
address = 'C:\\Users\\aucur\\PycharmProjects\\pythonProject\\corn\\'

# state마다 5*7*4회 시행, year마다 7*4회 시행, month마다 4회 시행
st, ye, mo = 0, 0, 0 # 각각 state, year, month에 해당하는 index
for n in range(1, 13*5*7*4+1):
    s = Select(driver.find_element_by_id('region'))
    s.select_by_visible_text(states[st])
    y = Select(driver.find_element_by_id('year'))
    y.select_by_visible_text(years[ye])
    m = Select(driver.find_element_by_id('month'))
    m.select_by_visible_text(months[mo])
    ''' state, year, month마다 각 parameter별로 csv파일 다운로드 후 합치기'''
    for i in range(0, 4):
        parameter = parameters[i]
        p = Select(driver.find_element_by_id('parameter'))
        p.select_by_visible_text(parameter)
        driver.find_element_by_xpath('//*[@id="submit"]').click()  # plot
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="csv-download"]/img').click()  # download csv
        time.sleep(1)
        rename(r"C:\Users\aucur\Downloads", 'part' + str(i))
        if i == 0:
            df_origin = pd.read_csv(address + 'part0', header=None, names=['A', 'B', 'C', 'D', 'E', 'F'])
        elif i == 1:
            df_other = pd.read_csv(address + 'part1', header=None, names=['A', 'B', 'C', 'D', 'E', 'F'])
            df_origin.D = df_other.C
        elif i == 2:
            df_other = pd.read_csv(address + 'part2', header=None, names=['A', 'B', 'C', 'D', 'E', 'F'])
            df_origin.E = df_other.C
        elif i == 3:
            df_other = pd.read_csv(address + 'part3', header=None, names=['A', 'B', 'C', 'D', 'E', 'F'])
            df_origin.F = df_other.C
    # 4개 다 합친 후 특정 행열 값 변경
    df_origin.iloc[3, 2] = 'Average Temperature'
    df_origin.iloc[3, 3] = 'Maximum Temperature'
    df_origin.iloc[3, 4] = 'Minimum Temperature'
    df_origin.iloc[3, 5] = 'Precipitation'
    '''data frame에서 csv 파일로 변경 '''
    df_origin.to_csv(path_or_buf=address + states[st] + '_' + years[ye] + '_' + months[mo] + '.csv', index=False,
                     header=False)
    if n % (5*7*4) == 0:
        st += 1
        ye += 1
        mo += 1
    elif n % (7*4) == 0:
        ye += 1
        mo += 1
    elif n % 4 == 0:
        mo += 1


'''
for state in states:
    s = Select(driver.find_element_by_id('region'))
    s.select_by_visible_text(state)
    for year in years:
        y = Select(driver.find_element_by_id('year'))
        y.select_by_visible_text(year)
        for month in months:
            m = Select(driver.find_element_by_id('month'))
            m.select_by_visible_text(month)
            for i in range(0, 4):
                parameter = parameters[i]
                p = Select(driver.find_element_by_id('parameter'))
                p.select_by_visible_text(parameter)
                driver.find_element_by_xpath('//*[@id="submit"]').click()  # plot
                time.sleep(1)
                driver.find_element_by_xpath('//*[@id="csv-download"]/img').click()  # download csv
                time.sleep(1)
                rename("C:\\Users\\aucur\\Downloads", 'part' + str(i))
                if i == 0:
                    df_origin = pd.read_csv(address + 'part0', header=None, names=['A','B','C','D','E','F'])
                elif i == 1:
                    df_other = pd.read_csv(address + 'part1', header=None, names=['A','B','C','D','E','F'])
                    df_origin.D = df_other.C
                elif i == 2:
                    df_other = pd.read_csv(address + 'part2', header=None, names=['A','B','C','D','E','F'])
                    df_origin.E = df_other.C
                elif i == 3:
                    df_other = pd.read_csv(address + 'part3', header=None, names=['A','B','C','D','E','F'])
                    df_origin.F = df_other.C

            # 4개 다 합치고 마지막에 특정 행열 값 변경
            df_origin.iloc[3, 2] = 'Average Temperature'
            df_origin.iloc[3, 3] = 'Maximum Temperature'
            df_origin.iloc[3, 4] = 'Minimum Temperature'
            df_origin.iloc[3, 5] = 'Precipitation'
            df_origin.to_csv(path_or_buf=address + str(state) + '_' + str(year) + '_' + str(month)+ '.csv', index=False, header=False)
            '''
