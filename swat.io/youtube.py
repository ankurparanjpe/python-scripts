from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import ctypes

print("Starting Youtube follower search")
df = pd.read_csv("socialmedias_yt.csv", sep=';',encoding='unicode_escape')

company = list(df.company)
youtube = list(df.youtube)
i=0
driver = webdriver.Chrome('D:/python scripts/chromedriver.exe')
for link in youtube:
    try:
        time.sleep(2)
        driver.get(str(youtube[i]))
        time.sleep(2)
        yt_count = driver.find_element_by_id('subscriber-count').text   #how to get exact count in youtube???
        print(yt_count.split(' ')[0])
        i += 1


    except Exception as e:
        print("problem in "+ company[i])
        i += 1
