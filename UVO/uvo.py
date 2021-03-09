from selenium import webdriver
import time
from datetime import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import ctypes

from selenium.webdriver.support.select import Select

print("Alert! Please make sure the customer provided doesnt have any system number alloted!!")
print("Give your token!")
df = pd.read_csv("uvo.csv", sep=',', encoding='unicode_escape')
customer = list(df.customer_no)
uvo = list(df.uvo)
provider = list(df.provider)
additional = list(df.additional)
system_no = 100
i=0


now = datetime.now()
today = now.strftime("%d.%m.%Y")


driver = webdriver.Chrome("D:/python scripts/chromedriver.exe")
driver.maximize_window()
#logging into brodos.net - working perfectly
driver.get("https://www.brodos.net/index.php?login=1")
driver.find_element_by_xpath('//*[@id="username"]').send_keys('ankur.paranjpe')
driver.find_element_by_xpath('//*[@id="password"]').send_keys(str(123456)+"\n")
#driver.implicitly_wait(10)
#driver.find_element_by_xpath('//*[@id="token"]').send_keys(token+"\n")
time.sleep(3)




for c in customer:
    try:
        driver.find_element_by_xpath('//*[@id="systemTopButtonShow"]').click()
        time.sleep(0.5)
        driver.find_element_by_xpath('//*[@id="ChangeSystemId"]').send_keys(str(1)+"\n")
        time.sleep(3)
        driver.get('https://www.brodos.net/index.php/mpath/stamm_deb_search')
        driver.find_element_by_xpath('//*[@id="searchcustomernofieldid"]').send_keys(str(customer[i])+"\n")

        try:
            time.sleep(3)
            driver.find_element_by_xpath('//*[@id="ext-gen141"]/div[1]/table/tbody/tr/td[1]').click()
            time.sleep(2)
            system_no = driver.find_element_by_xpath('//*[@id="module_frame"]/form[1]/table[3]/tbody/tr/td[1]/table/tbody/tr[1]/td[2]/div[2]').text
            system_no = system_no.split(": ")
            system_no = system_no[1]
            print(system_no)
            
        except Exception:
            time.sleep(3)
            system_no = driver.find_element_by_xpath('//*[@id="module_frame"]/form[1]/table[3]/tbody/tr/td[1]/table/tbody/tr[1]/td[2]/div[2]').text
            system_no = system_no.split(": ")
            system_no = system_no[1]
            print(system_no)
            
        driver.find_element_by_xpath('//*[text()="brodos Distribution (1)"]').click()
        time.sleep(0.5)
        driver.find_element_by_xpath('//*[@id="ChangeSystemId"]').send_keys(str(system_no)+"\n")
        time.sleep(3)
        driver.get('https://www.brodos.net/index.php/mpath/bactivate_stammtab_bactivateprovider')
        driver.find_element_by_xpath('//*[@id="module_frame"]/form/table[2]/tbody/tr/td[1]/table/tbody/tr/td[1]/button/img').click()
        driver.find_element_by_xpath('//*[@id="module_frame"]/form/table[3]/tbody/tr/td[1]/table/tbody/tr[1]/td[2]/select').click()
        #driver.find_element_by_partial_link_text(f'{provider[i]}').click()
        time.sleep(1)
        p = f"{provider[i]}"
        print(f"{provider[i]}" + " - brodos Distribution")
        driver.find_element_by_css_selector('[title*= "%s"]' %p).click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="module_frame"]/form/table[2]/tbody/tr/td[1]/table/tbody/tr/td[1]/button/img').click()
        driver.get('https://www.brodos.net/index.php/mpath/internaldata_intowndata')
        driver.find_element_by_xpath('//*[text()="Main sales partners"]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="module_frame"]/form[1]/table[5]/tbody/tr/td[1]/table/tbody/tr/td[1]/button/img').click()
        driver.find_element_by_xpath('//*[@id="module_frame"]/form[1]/table[6]/tbody/tr/td[1]/table/tbody/tr[1]/td[2]/select').click()
        driver.find_element_by_css_selector('[title*= "%s"]' %p).click()
        driver.find_element_by_xpath('//*[@id="module_frame"]/form[1]/table[6]/tbody/tr/td[1]/table/tbody/tr[2]/td[2]/input').send_keys(f'{uvo[i]}')
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="module_frame"]/form[1]/table[6]/tbody/tr/td[1]/table/tbody/tr[4]/td[2]/input').click()
        driver.find_element_by_xpath('//*[@id="module_frame"]/form[1]/table[6]/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/input').send_keys(today)
        driver.find_element_by_xpath('//*[@id="module_frame"]/form[1]/table[6]/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/input').send_keys('31.12.2030')
        driver.find_element_by_xpath('//*[@id="module_frame"]/form[1]/table[5]/tbody/tr/td/table/tbody/tr/td[1]/button/img').click()
        i+=1

    except Exception as e:
        print('problem with ' +  f'{customer[i]}')
        i+=1

driver.quit()
