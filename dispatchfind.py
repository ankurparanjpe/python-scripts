from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re

df = pd.read_csv("D:/python scripts/ordernumbers.csv")
sites = df.orders


print ("give token")
#token = input()

driver = webdriver.Chrome("E:/onlineshop images/onlineshop-support/res/chromedriver.exe")
driver.maximize_window()
driver.get("https://www.brodos.net/index.php?login=1")
driver.get("https://www.brodos.net/index.php?login=1")
driver.find_element_by_xpath('//*[@id="username"]').send_keys('ankur.paranjpe')
driver.find_element_by_xpath('//*[@id="password"]').send_keys(str(123456)+"\n")
driver.implicitly_wait(10)
#time.sleep(2)
#driver.find_element_by_name("token").send_keys(token)
#driver.find_element_by_xpath('//*[@id="ext-gen38"]').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="ext-gen9"]').click()
driver.find_element_by_xpath('//*[@id="ChangeSystemId"]').send_keys(str(1)+"\n")

time.sleep(5)
driver.get('https://www.brodos.net/index.php/mpath/svoucher_sales_salorder/')
    
for order in sites:
    driver.find_element_by_xpath('//*[@id="modulecontent"]/table/tbody/tr[5]/td[2]/input').send_keys(order)
    driver.find_element_by_xpath('//*[@id="modulecontent"]/table/tbody/tr[9]/td[2]/table/tbody/tr/td/input').click()
    time.sleep(5)

    try:
        ordernumber = driver.find_element_by_xpath('//*[@id="modulecontent"]/table/tbody/tr[2]/td[1]/table/tbody/tr/td[2]/table/tbody/tr[2]/td[2]')
        print(ordernumber.text)
    except Exception as e:
        print(f"{order} not found")
        
    driver.find_element_by_xpath('//*[@id="module_frame"]/form[1]/table[2]/tbody/tr/td[1]/table/tbody/tr/td[1]/button/img').click()
    
driver.quit()



