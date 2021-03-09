from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import ctypes

print("Starting Instagram follower search")
df = pd.read_csv("socialmedias_insta.csv", sep=';',encoding='unicode_escape',error_bad_lines=False)

company = list(df.company)
instagram = list(df.instagram)
i=0
driver = webdriver.Chrome('D:/python scripts/chromedriver.exe')
driver.get('https://www.instagram.com/accounts/login/')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[5]/button/span[2]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="email"]').send_keys('ankurparanjpe1010@gmail.com')
driver.find_element_by_xpath('//*[@id="pass"]').send_keys('qu@ke6arena')
driver.find_element_by_xpath('//*[@id="loginbutton"]').click()
time.sleep(10)


for link in instagram:
    try:
        driver.get(str(instagram[i]))
        action = ActionChains(driver)
        time.sleep(2)      
        element = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span')
        title = element.get_attribute("title");
        print (title)
        i += 1


    except Exception as e:
        print("problem in " + company[i])
        i += 1
