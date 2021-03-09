from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd

print ("Here we go!")
df = pd.read_csv("D:/Python projects/Brodosprojects/OStheme/theme.csv", sep=',')
 
sites = df.url
theme = list(df.theme)
i=0
j=0
k=0

for url in sites:
    try:
        driver = webdriver.Chrome("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Python 3.7\chromedriver.exe")
        driver.get("https://"+url+"/user")
        driver.maximize_window()

        driver.find_element_by_name("name").send_keys("amit")
        driver.find_element_by_name("pass").send_keys("admin@"+"\n")
        driver.find_element_by_xpath('//*[@id="block-system-user-menu"]/ul/li[4]/a').click()
        if i < 101:
            driver.find_element_by_xpath('//*[@id="edit-back-ground-color-of-menu-inner_wrapper"]/div').click()
            time.sleep(3)
            driver.find_element_by_xpath('/html/body/div[8]/div[5]/input').send_keys(Keys.CONTROL + 'a')
            time.sleep(3)
            driver.find_element_by_xpath('/html/body/div[8]/div[5]/input').send_keys(theme[i])
            time.sleep(3)
            driver.find_element_by_xpath('//*[@id="edit-submit"]').click()
            time.sleep(3)
            driver.find_element_by_xpath('//*[@id="block-system-user-menu"]/ul/li[6]/a').click()
            i+=1
            driver.quit()
            print(str(url)+ "has successfully changed the theme!")

    except:
        print("something is wrong with shop " + str(url) + " or script")
        continue
