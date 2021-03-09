from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd

print("Here we go!")
df = pd.read_csv("D:/000000000office/zmincontent/mincontent.csv", sep=',')
 
sites = df.url
shopname = list(df.shopname)
address = list(df.address)
zipcode = list(df.zipcode)
city = list(df.city)
email = list(df.email)
telephone = list(df.telephone)
owner = list(df.owner)
tax = list(df.tax)

i=0
j=0
k=0
l=0
m=0
n=0
o=0
p=0

for url in sites:
    try:
        driver = webdriver.Chrome("D:/000000000office/zUsername/chromedriver_win32/chromedriver.exe")
        driver.get("https://"+url+"/user")
        driver.maximize_window()
        driver.find_element_by_name("name").send_keys("amit")
        driver.find_element_by_name("pass").send_keys("7565sw3su"+"\n")
        driver.find_element_by_xpath('//*[@id="block-system-user-menu"]/ul/li[2]/a').click()
        if i <101:
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="popup-buttons"]/button[1]').click()
            driver.find_element_by_xpath('//*[@id="edit-title"]').send_keys(Keys.CONTROL + 'a')
            driver.find_element_by_xpath('//*[@id="edit-title"]').send_keys(shopname[i])
            driver.find_element_by_xpath('//*[@id="edit-field-shop-name-und-0-organisation-name"]').send_keys(Keys.CONTROL + 'a')
            driver.find_element_by_xpath('//*[@id="edit-field-shop-name-und-0-organisation-name"]').send_keys(shopname[i])
            i += 1
            if j <101:
                driver.find_element_by_xpath('//*[@id="edit-field-shop-name-und-0-thoroughfare"]').send_keys(Keys.CONTROL + 'a')
                driver.find_element_by_xpath('//*[@id="edit-field-shop-name-und-0-thoroughfare"]').send_keys(address[j])
                driver.find_element_by_xpath('//*[@id="edit-field-shop-name-und-0-premise"]').send_keys(Keys.CONTROL + 'a')
                driver.find_element_by_xpath('//*[@id="edit-field-shop-name-und-0-premise"]').send_keys(" ")
                j += 1
                if k <101:
                    driver.find_element_by_xpath('//*[@id="edit-field-shop-name-und-0-postal-code"]').send_keys(Keys.CONTROL + 'a')
                    driver.find_element_by_xpath('//*[@id="edit-field-shop-name-und-0-postal-code"]').send_keys(zipcode[k])
                    k +=1
                    if l <101:
                        driver.find_element_by_xpath('//*[@id="edit-field-shop-name-und-0-locality"]').send_keys(Keys.CONTROL + 'a')
                        driver.find_element_by_xpath('//*[@id="edit-field-shop-name-und-0-locality"]').send_keys(city[l])
                        l +=1
                        if m<101:
                            driver.find_element_by_xpath('//*[@id="edit-field-telephone-number-und-0-value"]').send_keys(Keys.CONTROL + 'a')
                            driver.find_element_by_xpath('//*[@id="edit-field-telephone-number-und-0-value"]').send_keys(telephone[m])
                            driver.find_element_by_xpath('//*[@id="edit-field-fax-number-und-0-value"]').send_keys(Keys.CONTROL + 'a')
                            driver.find_element_by_xpath('//*[@id="edit-field-fax-number-und-0-value"]').send_keys(" ")
                            m +=1
                            if n <101:
                                driver.find_element_by_xpath('//*[@id="edit-field-shop-email-und-0-email"]').send_keys(Keys.CONTROL + 'a')
                                driver.find_element_by_xpath('//*[@id="edit-field-shop-email-und-0-email"]').send_keys(email[n])
                                n +=1
                                if o <101:
                                    driver.find_element_by_xpath('//*[@id="edit-field-gesch-ftsf-hrer-und-0-value"]').send_keys(Keys.CONTROL + 'a')
                                    driver.find_element_by_xpath('//*[@id="edit-field-gesch-ftsf-hrer-und-0-value"]').send_keys(owner[o])
                                    o +=1
                                    if p <101:
                                        driver.find_element_by_xpath('//*[@id="edit-field-umsatzsteuergesetz-und-0-value"]').send_keys(Keys.CONTROL + 'a')
                                        driver.find_element_by_xpath('//*[@id="edit-field-umsatzsteuergesetz-und-0-value"]').send_keys(tax[p])
                                        p +=1
                                        driver.find_element_by_xpath('//*[@id="edit-submit"]').click()
                                        driver.find_element_by_xpath('//*[@id="block-system-user-menu"]/ul/li[6]/a').click()
                                        print (str(url) + " has address details successfully filled.")
                                        driver.quit()
				
    except:
        i += 1
        j += 1
        k += 1
        l += 1
        m += 1
        n += 1
        o += 1
        p += 1
        print("Something went wrong with " + str(url) + " Script broken or Shop is not in proper format.")
        continue
    
