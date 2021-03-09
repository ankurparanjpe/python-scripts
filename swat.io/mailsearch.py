from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import ctypes

print("Starting email search")
df = pd.read_csv("socialmedias_mails.csv", sep=';',encoding='unicode_escape')

company = list(df.company)
website = list(df.website)
i=0
driver = webdriver.Chrome('D:/python scripts/chromedriver.exe')



for link in website:
    try:
        driver.get(str(website[i]))
        time.sleep(3)
        driver.find_element_by_xpath("//*[contains(text(), 'Impressum')]").click()
        mails = driver.find_element_by_xpath("//*[contains(text(), '@')]")
        for mail in mails:
            print(mail.text)

        i += 1


    except Exception as e:
        print(e)
        i += 1
