from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd

print("Here we go!")
df = pd.read_csv("manually_done.csv", sep='\n')

orders = df.orders
i=0
    
if i < 101:
    try:
        driver = webdriver.Chrome("E:/onlineshop images/onlineshop-support/res/chromedriver.exe")
        
        driver.maximize_window()
        driver.get("http://ordercontext.brodos.net/olm/ui?order=" + str(orders[i]))
        driver.find_element_by_xpath('//*[@id="gwt-uid-3"]').send_keys(Keys.CONTROL + 'a')
        driver.find_element_by_xpath('//*[@id="gwt-uid-3"]').send_keys('ankur.paranjpe')
        driver.find_element_by_xpath('//*[@id="gwt-uid-5"]').send_keys(Keys.CONTROL + 'a')
        driver.find_element_by_xpath('//*[@id="gwt-uid-5"]').send_keys('123456')
        driver.find_element_by_xpath('//*[@id="olmlogin-468295481"]/div/div[2]/div/div/div/div[3]/div/table/tbody/tr[3]/td[3]/div/div/div').click() 
        time.sleep(3)
        driver.get(f"http://ordercontext.brodos.net/olm/ui?order={orders}")
        time.sleep(3)
        driver.find_element_by_xpath('find_element_by_xpath').click()
        driver.find_element_by_xpath('//*[@id="olmui-105836740-overlays"]/div[3]/div/div/div[3]/div/div/div/div[1]/textarea').send_keys("Delivered")
        print(f"Order {order} is set as manually done!!!")
        driver.quit()
        i += 1
        
    except Exception as e:
        print(str(e))
        i += 1
    
