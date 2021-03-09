from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


print ("Here we go!")
df = pd.read_csv("D:/000000000office/zMenu Point/addmenu.csv")
sites = df.url
menu = list(df.anfahrt)
i = 0

for url in sites:
    try:
        driver = webdriver.Chrome("D:/000000000office/zUsername/chromedriver_win32/chromedriver.exe")
        driver.get("https://"+url+"/user")
        driver.maximize_window()

        driver.find_element_by_name("name").send_keys("amit")
        driver.find_element_by_name("pass").send_keys("7565sw3su"+"\n")
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="popup-buttons"]/button[1]').click()
        if i < 101:
            driver.find_element_by_link_text('Anfahrt').click()
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/div[5]/div/div[3]/div/div/ul/li[2]/a').click()
            time.sleep(5)
            driver.find_element_by_xpath('//*[@id="cke_13"]').click()
            driver.find_element_by_xpath('//*[@id="cke_1_contents"]/textarea').click()
            driver.find_element_by_xpath('//*[@id="cke_1_contents"]/textarea').send_keys(Keys.CONTROL + 'a')
            driver.find_element_by_xpath('//*[@id="cke_1_contents"]/textarea').send_keys("<h1>Anfahrt</h1><p>So findet ihr zu uns:</p><p>"+menu[i])
            driver.find_element_by_xpath('//*[@id="edit-submit"]').click()
            driver.find_element_by_xpath('//*[@id="block-system-user-menu"]/ul/li[6]/a').click()
            print(f"{url} has successfully added direction point!")
            driver.quit()
            i += 1

    except Exception as e:
        i += 1
        print (str(e))
        continue
