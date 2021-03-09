from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd


print("Starting Linkedin follower search")
df = pd.read_csv("socialmedias_linkedin.csv", sep=';',encoding='unicode_escape')

company = list(df.company)
linkedin = list(df.linkedin)
i=0
driver = webdriver.Chrome('D:/python scripts/chromedriver.exe')
driver.get('https://www.linkedin.com/login')
driver.find_element_by_xpath('//*[@id="username"]').send_keys('ankurparanjpe10@gmail.com')
driver.find_element_by_xpath('//*[@id="password"]').send_keys('quake6arena')
driver.find_element_by_xpath('//*[@id="app__container"]/main/div[2]/form/div[3]/button').click()

for link in linkedin:
    try:
        time.sleep(3)
        driver.get(str(linkedin[i]))
        time.sleep(2)
        linkedin_count = driver.find_element_by_css_selector('.t-20.t-black').text
        print(linkedin_count.split(' ')[0])
        i += 1


    except Exception as e:
        print("problem in company" + str(company[i]))
        i+=1
