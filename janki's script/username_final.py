from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd

print ("Here we go!")
df = pd.read_csv("D:/000000000office/zUsername/username.csv", sep=',')
 
sites = df.url
username = list(df.username)
email = list(df.email)
password = list(df.password)
i=0
j=0
k=0

for url in sites:
    try:
        driver = webdriver.Chrome("D:/000000000office/zUsername/chromedriver_win32/chromedriver.exe")
        driver.get("https://"+url+"/user")
        driver.maximize_window()

        driver.find_element_by_name("name").send_keys("admin")
        driver.find_element_by_name("pass").send_keys("3Kc9wAweBsnj"+"\n")
        driver.get("https://"+url+'/de/admin/people')
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="popup-buttons"]/button[1]').click()
        driver.find_element_by_xpath('//*[@id="content"]/ul/li/a').click()
        time.sleep(2)
    
        if  i < 101:
            driver.find_element_by_xpath('//*[@id="edit-name"]').send_keys(username[i])
            i += 1
            if j < 101:
                driver.find_element_by_xpath('//*[@id="edit-mail"]').send_keys(email[j]) 
                j += 1
                if k < 101:
                    driver.find_element_by_xpath('//*[@id="edit-pass-pass1"]').send_keys(password[k])
                    driver.find_element_by_xpath('//*[@id="edit-pass-pass2"]').send_keys(password[k])
                    k +=1
                    time.sleep(1)
                    driver.find_element_by_xpath('//*[@id="edit-roles-8"]').click()
                    driver.find_element_by_xpath('//*[@id="edit-admin-language-de"]').click()
                    driver.find_element_by_xpath('//*[@id="edit-language-de"]').click()
                    driver.find_element_by_xpath('//*[@id="edit-submit"]').click()
                    time.sleep(2)
                    driver.find_element_by_xpath('//*[@id="toolbar-user"]/li[2]/a').click()
                    print(str(url) + " has user name now.")
                    driver.quit()

    except:
        i += 1
        j += 1
        k += 1
        print(str(url) + " has issue in shop or in script.")
        continue
    
