import time, os, shutil
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
import glob

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
time_scale = '1-Month' # default

for state in states:
    s = Select(driver.find_element_by_id('region'))
    s.select_by_visible_text(state)
    for year in years:
        y = Select(driver.find_element_by_id('year'))
        y.select_by_visible_text(year)
        for month in months:
            m = Select(driver.find_element_by_id('month'))
            m.select_by_visible_text(month)
            for i in (1, 2, 3, 4):
                parameter = parameters[i-1]
                p = Select(driver.find_element_by_id('parameter'))
                p.select_by_visible_text(parameter)
                driver.find_element_by_xpath('//*[@id="submit"]').click()
                time.sleep(0.5)
                driver.find_element_by_xpath('//*[@id="csv-download"]/img').click()
                time.sleep(0.5)
                rename(r"C:\Users\aucur\Downloads", 'part' + i)

            path = r"C:\Users\aucur\Downloads"
            read_data = os.listdir(path)
            findfile = 'part' + '*.csv'
            data_list = glob.glob(os.path.join(path, findfile))

            encoding = 'EUC-kr'


            for files in data_list:
                df = pd.read_csv(files, encoding = 'EUL-KF=r')

            dataCombine = pd.DataFrame()

            rename(r"C:\Users\aucur\Downloads", state + '_' + parameter + '_' + year + '_' + month + '.csv')
