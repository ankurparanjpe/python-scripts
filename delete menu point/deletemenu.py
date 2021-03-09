from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import logging
logging.basicConfig(filename = 'test.log', level = logging.DEBUG)

print ("Here we go!")
df = pd.read_csv("D:/python scripts/delete menu point/deletemenu.csv")
sites = df.url
i = 0

for url in sites:
    driver = webdriver.Chrome("E:/onlineshop images/onlineshop-support/res/chromedriver.exe")
    try:
        if i < 100:
            driver.get("https://" + url + "/user")
            driver.maximize_window()

            driver.find_element_by_name("name").send_keys("amit")
            driver.find_element_by_name("pass").send_keys("7565sw3su" + "\n")
            time.sleep(3)
            driver.find_element_by_xpath('//*[@id="popup-buttons"]/button[1]').click()
            time.sleep(1)
            driver.find_element_by_link_text('Über uns').click()
            time.sleep(1)
            driver.find_element_by_link_text('Bearbeiten').click()
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="edit-delete"]').click()
            time.sleep(1)

            driver.find_element_by_link_text('Anfahrt').click()
            time.sleep(1)
            driver.find_element_by_link_text('Bearbeiten').click()
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="edit-delete"]').click()
            time.sleep(1)

            driver.find_element_by_link_text('Kontakt').click()
            time.sleep(1)
            driver.find_element_by_link_text('Bearbeiten').click()
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="edit-delete"]').click()
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="block-system-user-menu"]/ul/li[6]/a')

            driver.quit()
            logging.info (f"{url} has deleted multiple menu points!")
    except Exception as e:
        print (str(e))
        continue
