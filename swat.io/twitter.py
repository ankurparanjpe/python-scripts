from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import ctypes

print("Starting twitter follower search")
df = pd.read_csv("socialmedias_twitter.csv", sep=';',encoding='unicode_escape')

company = list(df.company)
twitter = list(df.twitter)
i=0
driver = webdriver.Chrome('D:/python scripts/chromedriver.exe')
for link in twitter:
    try:
        driver.get(str(twitter[i]))
        action = ActionChains(driver)
        time.sleep(5)      
        element = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[1]/div/div[5]/div[2]/a')
        title = element.get_attribute("title")
        print (title)
        i += 1


    except Exception as e:
        print("problem with "+ company[i])
        i += 1
