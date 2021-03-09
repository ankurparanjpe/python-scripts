from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import ctypes

print("Alert! Please make sure the customer provided doesnt have any system number alloted!!")
print("Give your token!")
df = pd.read_csv("tenant.csv", sep=',', encoding='unicode_escape')
token = input()
tenant = list(df.tenant)
i=0

driver = webdriver.Chrome("E:/onlineshop images/onlineshop-support/res/chromedriver.exe")
driver.maximize_window()
#logging into brodos.net - working perfectly
driver.get("https://www.brodos.net/index.php?login=1")
driver.find_element_by_xpath('//*[@id="username"]').send_keys('ankur.paranjpe')
driver.find_element_by_xpath('//*[@id="password"]').send_keys(str(123456)+"\n")
#driver.implicitly_wait(10)
#driver.find_element_by_xpath('//*[@id="token"]').send_keys(token+"\n")

time.sleep(3)
driver.find_element_by_xpath('//*[text()="Demo - System (950)"]').click()
time.sleep(0.5)

for i in range(0,75):

    driver.find_element_by_xpath('//*[@id="ChangeSystemId"]').send_keys(str(tenant[i])+"\n")
    time.sleep(3)
    driver.get('https://www.brodos.net/index.php/mpath/internaldata_intowndata')
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="module_frame"]/form[1]/table[2]/tbody/tr/td[1]/table/tbody/tr/td/button/img').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="module_frame"]/form[1]/table[3]/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/input').send_keys(Keys.CONTROL + 'a')
    driver.find_element_by_xpath('//*[@id="module_frame"]/form[1]/table[3]/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/input').send_keys("+49(0)91337770-600")
    driver.find_element_by_xpath('//*[@id="module_frame"]/form[1]/table[3]/tbody/tr/td[2]/table/tbody/tr[4]/td[2]/input').send_keys(Keys.CONTROL + 'a')
    driver.find_element_by_xpath('//*[@id="module_frame"]/form[1]/table[3]/tbody/tr/td[2]/table/tbody/tr[4]/td[2]/input').send_keys("+49(0)91337770-600")
    driver.find_element_by_xpath('//*[@id="module_frame"]/form[1]/table[2]/tbody/tr/td/table/tbody/tr/td[1]/button/img').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="ext-gen9"]').click()
    i+=1

driver.close()

        
