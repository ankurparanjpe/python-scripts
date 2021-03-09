from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd

print ("give url without https")
df = pd.read_csv("D:/python scripts/freepaket.csv")
sites = df.url


for url in sites:
    driver = webdriver.Chrome("E:/onlineshop images/onlineshop-support/res/chromedriver.exe")
    driver.get("https://"+url+"/user")
    driver.maximize_window()

    driver.find_element_by_name("name").send_keys("admin")
    driver.find_element_by_name("pass").send_keys("3Kc9wAweBsnj"+"\n")
    strukture = driver.find_element_by_id("toolbar-link-admin-structure")
    ActionChains(driver).double_click(strukture).perform()
    driver.implicitly_wait(5)

    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL+'t')
    driver.implicitly_wait(5)
    driver.get("https://" + url + "/admin/structure/osw_features_footer/manage")
    driver.implicitly_wait(5)
    driver.find_element_by_xpath('//*[@id="edit-paket-administration-free-paket"]').click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath('//*[@id="popup-buttons"]/button[1]').click()
    driver.implicitly_wait(100)
    driver.find_element_by_xpath('//*[@id="edit-submit"]').click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath('//*[@id="toolbar-user"]/li[2]/a').click()
    driver.quit()

print (url + "Done")
