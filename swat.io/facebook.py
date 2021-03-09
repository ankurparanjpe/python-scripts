from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import ctypes

print("Starting Facebook follower search")
df = pd.read_csv("socialmedias_fb.csv", sep=';',encoding='unicode_escape')

company = list(df.company)
fb = list(df.facebook)
i=0
driver = webdriver.Chrome('D:/python scripts/chromedriver.exe')

driver.get('https://www.facebook.com/')
driver.find_element_by_xpath('//*[@id="email"]').send_keys('ankurparanjpe1010@gmail.com')
driver.find_element_by_xpath('//*[@id="pass"]').send_keys('qu@ke6arena')
driver.find_element_by_xpath('//*[@id="u_0_b"]').click()

for link in fb:
    try:
        time.sleep(1)
        driver.get(str(fb[i]))
        time.sleep(2)
        fb_count = driver.find_element_by_xpath("//*[contains(text(), 'people follow this')]")   #how to get exact count in youtube???
        print(fb_count.text)
        i += 1


    except Exception as e:
        print("pronblem with " + company[i])
        i += 1
