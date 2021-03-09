from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import ctypes

print("Starting xing follower search")
df = pd.read_csv("socialmedias_xing.csv", sep=';',encoding='unicode_escape')

company = list(df.company)
xing = list(df.xing)
i=0

driver = webdriver.Chrome('D:/python scripts/chromedriver.exe')
driver.get('https://login.xing.com/')
time.sleep(3)
driver.find_element_by_xpath('//*[@id="consent-accept-button"]/div/span').click()
driver.find_element_by_xpath('//*[@id="username"]').send_keys('sakurpazi@gmail.com')
driver.find_element_by_xpath('//*[@id="password"]').send_keys('sakur@852')
driver.find_element_by_xpath('//*[@id="javascript-content"]/div[2]/form/div[5]/button').click()


for link in xing:
    try:
        time.sleep(3)
        driver.get(str(xing[i]))
        time.sleep(2)
        xing_count = driver.find_element_by_id('employees-tab').text
        print(xing_count.split(' ')[1])
        i += 1


    except Exception as e:
        print("problem with " + company[i])
        i += 1
