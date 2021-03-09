from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException


print("Give your token!")
df = pd.read_csv("system_creation.csv", sep=',')
token = input()
system = list(df.system_no)
company = list(df.company)
address = list(df.address)
zipcode = list(df.zipcode)
city = list(df.city)
telephone = list(df.telephone)
admin = list(df.admin)
customer = list(df.customer_no)

try:
    driver = webdriver.Chrome("C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Python 3.7/chromedriver.exe")
    #logging into brodos.net - working perfectly
    driver.get("https://www.brodos.net/index.php?login=1")
    driver.find_element_by_xpath('//*[@id="username"]').send_keys('ankur.paranjpe')
    driver.find_element_by_xpath('//*[@id="password"]').send_keys('1234567')
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="token"]').send_keys(token+"\n")
    time.sleep(2)
    #going to system 1 for cross deb connection (not sure yet)
    driver.find_element_by_xpath('//*[@id="ext-gen9"]').click()
    driver.find_element_by_xpath('//*[@id="ChangeSystemId"]').send_keys(str(1)+"\n")
    time.sleep(3)
    driver.get('https://www.brodos.net/index.php/mpath/stamm_deb_search')
    driver.find_element_by_xpath('//*[@id="ext-comp-1322"]').send_keys("telemaster")
    driver.find_element_by_xpath('//*[@id="ext-gen64"]').click()     #working perfectly until here, didnt knew how to wait its found or not

    try:
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="ext-gen141"]/div[1]/table/tbody/tr/td[1]/div').click()

    except:
        time.sleep(2.5)
        driver.find_element_by_xpath('//*[@id="module_frame"]/form[1]/table[2]/tbody/tr/td[1]/table/tbody/tr/td[3]/button/img').click()
        driver.find_element_by_xpath('//*[@id="module_frame"]/form[1]/table[3]/tbody/tr/td[1]/table/tbody/tr[1]/td[2]/div[2]/input').send_keys(str(system[0]))
        driver.find_element_by_xpath('//*[@id="ext-gen31"]/img').click()

except Exception as e:
    print(str(e))
