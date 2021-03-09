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
import logging
from selenium.webdriver.chrome.options import Options

logging.basicConfig(filename='D:/python scripts/test.log')

df = pd.read_csv("D:/python scripts/ordernumbers.csv")
sites = df.orders


logging.warning("give token")
print("give token")
token = input()
options = Options()
options.headless = True
driver = webdriver.Chrome("D:\python scripts\chromedriver.exe",options=options)
driver.maximize_window()
driver.get("https://www.brodos.net/index.php?login=1")
driver.get("https://www.brodos.net/index.php?login=1")
driver.find_element_by_xpath('//*[@id="login_username"]').send_keys('ankur.paranjpe')
driver.find_element_by_xpath('//*[@id="login_password"]').send_keys(str(123456)+"\n")
driver.implicitly_wait(10)
#time.sleep(2)
#driver.find_element_by_name("token").send_keys(token)
#driver.find_element_by_xpath('//*[@id="ext-gen38"]').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="ext-gen9"]').click()
driver.find_element_by_xpath('//*[@id="ChangeSystemId"]').send_keys(str(1)+"\n")

time.sleep(5)
driver.get('https://www.brodos.net/index.php/mpath/svoucher_sales_saldelivery/')
    
for order in sites:
    driver.find_element_by_xpath('//*[@id="module_frame"]/form[1]/table[3]/tbody/tr[8]/td[2]/input').send_keys(order)
    driver.find_element_by_xpath('//*[@id="module_frame"]/form[1]/table[3]/tbody/tr[11]/td[2]/table/tbody/tr/td/input').click()
    time.sleep(2)

    try:
        ordernumber = driver.find_element_by_xpath('//*[@id="module_frame"]/form[1]/table[3]/tbody/tr[2]/td[1]/table/tbody/tr/td[2]/table/tbody/tr[3]/td[2]')
        logging.warning(ordernumber.text)
        number = driver.find_element_by_xpath('//*[@id="module_frame"]/form[1]/table[3]/tbody/tr[2]/td[1]/table/tbody/tr/td[3]/fieldset/div/ul/li/ul/li')
        print(str(ordernumber.text) + " " + str(number.text))
    except Exception as e:
        logging.warning(f"{order} not found")
        print(f"{order} not found")
        
        
    driver.find_element_by_xpath('//*[@id="module_frame"]/form[1]/table[2]/tbody/tr/td[1]/table/tbody/tr/td[1]/button/img').click()
    
driver.quit()

input()


