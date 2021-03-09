from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import ctypes
import csv
import os

i=0
j=0
driver = webdriver.Chrome('D:/python scripts/chromedriver.exe')
driver.get('https://www.oanda.com/fx-for-business/historical-rates')
driver.maximize_window()
driver.find_element_by_xpath('//*[@id="hcc"]/div[2]/div[1]/div[1]/ul/li[4]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="hcc"]/div[2]/div[1]/div[1]/ul/li[4]/div/div/ul/li[3]/div/div[1]').click()
time.sleep(1)



while i < 4:
    actions = ActionChains(driver)
    from_cur = ['PLN',"AED", "SAR", "KWD"]
    to_cur = ["EUR", "USD", "USD", "USD"]

    driver.find_element_by_xpath('//*[@id="havePicker"]/div/input').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="havePicker"]/div/input').send_keys(f"{from_cur[i]}" + Keys.DOWN + Keys.ENTER)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="hcc"]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div').click()
    time.sleep(3)
    print(f'{to_cur[j]}')
    actions.send_keys(f"{to_cur[j]}" + Keys.DOWN + Keys.ENTER)
    actions.perform()
    time.sleep(1)

    driver.find_element_by_xpath('//*[@id="hcc"]/div[2]/div[1]/div[3]/div/div[1]/div[1]/div[2]').click()
    time.sleep(3)
    table = driver.find_element_by_xpath('//*[@id="ht2"]/table')


    #rows.append([table])
    with open('abc.csv', 'w', encoding='utf8', newline='') as file:
        writer = csv.writer(file)
        for row in table.find_elements_by_css_selector('tr'):
            writer.writerow([d.text for d in row.find_elements_by_css_selector('td')])

    data = pd.read_csv("abc.csv", header=None)
    data.drop([0,1,2,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32], axis=0, inplace = True)
    print(data)
    df = data.rename(columns = {0:'date',1:'rate'})
    df.to_csv(f'{from_cur[i]}_{to_cur[j]}.csv', index=False)
    j+=1
    i+=1
    
os.remove('abc.csv')
driver.quit()
