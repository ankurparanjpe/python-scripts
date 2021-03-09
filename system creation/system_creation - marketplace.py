from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import ctypes

print("Alert! Please make sure the customer provided doesnt have any system number alloted!!")
print("Give your token!")
df = pd.read_csv("system_creation.csv", sep=',', encoding='unicode_escape')
token = input()
system = list(df.system_no)
company = list(df.company)
address = list(df.address)
zipcode = list(df.zipcode)
city = list(df.city)
telephone = list(df.telephone)
admin = list(df.admin)
customer = list(df.customer_no)
i=0

try:
    if i < 11:
        driver = webdriver.Chrome("D:/python scripts/chromedriver.exe")
        driver.maximize_window()
        #logging into brodos.net - working perfectly
        driver.get("https://www.brodos.net/index.php?login=1")
        driver.find_element_by_xpath('//*[@id="login_username"]').send_keys('ankur.paranjpe')
        driver.find_element_by_xpath('//*[@id="login_password"]').send_keys(str(123456) + '\n')
        #driver.implicitly_wait(10)
        #driver.find_element_by_xpath('//*[@id="token"]').send_keys(token+"\n")
    
        time.sleep(3)
        driver.find_element_by_xpath('//*[text()="Demo - System (950)"]').click()
        time.sleep(0.5)

        driver.find_element_by_xpath('//*[@id="ChangeSystemId"]').send_keys(str(100)+"\n")
        time.sleep(3)
        
        driver.get('https://www.brodos.net/index.php/mpath/ticket_zentrale')

        #commented out because it will give a popup a ticket fill form. Comment below out when going live - working perfectly
        driver.find_element_by_xpath('//*[text()="Create New Distributor"]').click()
        mainpage = driver.window_handles[0]
        print(mainpage)
        popup = driver.window_handles[1]
        driver.switch_to.window(popup)
        driver.find_element_by_xpath('//*[@id="name1"]').send_keys(str(company[i]))
        driver.find_element_by_xpath('/html/body/form/table/tbody/tr/td/table/tbody/tr[5]/td/table/tbody/tr[3]/td[2]/input[2]').send_keys(str(address[i]))
        driver.find_element_by_xpath('//*[@id="zipcode"]').send_keys(str(zipcode[i]))
        driver.find_element_by_xpath('//*[@id="city"]').send_keys(str(city[i]))
        driver.find_element_by_xpath('//*[@id="country"]/option[82]').click()
        driver.find_element_by_xpath('//*[@id="phone"]').send_keys(str(telephone[i]))
        driver.find_element_by_xpath('//*[@id="mobilephone"]').send_keys(str(telephone[i]))
        driver.find_element_by_xpath('//*[@id="email"]').send_keys(str(admin[i]))
        #enable this button clicker when testing live
        driver.find_element_by_xpath('/html/body/form/table/tbody/tr/td/table/tbody/tr[9]/td/table/tbody/tr[2]/td/input[1]').click()
        driver.switch_to.window(mainpage)
        print("Ticket created properly!")

        #section for system creation form - working perfectly
        driver.get('https://www.brodos.net/index.php/mpath/ticket_tic')
        driver.find_element_by_xpath('//*[@id="tbHeaderTable"]/tbody/tr[2]').click()
        driver.find_element_by_xpath('//*[@id="ticketlist"]/table[1]/tbody/tr/td[2]/a/img').click()
        driver.find_element_by_xpath('//*[@id="systemid"]').send_keys(str(system[i]))
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="systemname"]').send_keys(str(company[i]))
        driver.find_element_by_xpath('//*[@id="newsystemform"]/table[3]/tbody/tr[3]/td[2]/select/option[49]').click()
        driver.find_element_by_xpath('//*[@id="newsystemform"]/table[3]/tbody/tr[4]/td[2]/select/option[6]').click()
        driver.find_element_by_xpath('//*[@id="newsystemform"]/table[3]/tbody/tr[5]/td[2]/select/option[3]').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="TicketTypes"]/tbody/tr[1]/td[2]/input').send_keys('support@brodos.net')
        driver.find_element_by_xpath('//*[@id="TicketTypes"]/tbody/tr[2]/td[2]/input').send_keys('support@contentcard.com')
        driver.find_element_by_xpath('//*[@id="TicketTypes"]/tbody/tr[3]/td[2]/input').send_keys(str(admin[i]))
        driver.find_element_by_xpath('//*[@id="customerno"]').send_keys(Keys.CONTROL + 'a')
        driver.find_element_by_xpath('//*[@id="customerno"]').send_keys(str(50)+str(system[i]))
        driver.find_element_by_xpath('//*[@id="salutation"]/option[4]').click()
        time.sleep(3)
        #this will create new system, enable when going live.
        driver.find_element_by_xpath('//*[@id="create"]').click()
        print(f"System {str(system[i])} only created, going for other settings now!")

        #closing ticket - working perfectly
        driver.get('https://www.brodos.net/index.php/mpath/ticket_tic')
        driver.find_element_by_xpath('//*[@id="tbHeaderTable"]/tbody/tr[2]').click()
        driver.find_element_by_xpath('//*[@id="ticketcomment"]/table[3]/tbody/tr/td[1]/table/tbody/tr[2]/td[2]/select/option[4]').click()
        driver.find_element_by_xpath('//*[@id="ticketcomment"]/table[3]/tbody/tr/td[2]/table/tbody/tr/td[2]/textarea').send_keys('done')
        driver.find_element_by_xpath('//*[@id="ticketcomment"]/table[3]/tbody/tr/td[2]/table/tbody/tr/td[2]/input').click()
        print("Ticket closed!")

        #going to system 1 for cross deb connection
        time.sleep(3)
        driver.find_element_by_xpath('//*[text()="brodos (100)"]').click()
        time.sleep(0.5)
        driver.find_element_by_xpath('//*[@id="ChangeSystemId"]').send_keys(str(1)+"\n")
        time.sleep(3)
        driver.get('https://www.brodos.net/index.php/mpath/stamm_deb_create')
        driver.implicitly_wait(100)
        driver.find_element_by_xpath('//*[@id="ext-gen71"]/table[3]/tbody/tr/td[1]/table/tbody/tr[3]/td[2]/div[1]/select/option[4]').click()
        driver.implicitly_wait(100)
        driver.find_element_by_xpath('//*[@id="customerno"]').send_keys("CCD"+str(system[i]))
        driver.implicitly_wait(100)
        driver.find_element_by_xpath('//*[@id="module_frame"]/form[1]/table[3]/tbody/tr/td[1]/table/tbody/tr[1]/td[2]/div[2]/input').send_keys(str(system[i]))
        driver.find_element_by_xpath('//*[@id="module_frame"]/form[1]/table[3]/tbody/tr/td[1]/table/tbody/tr[4]/td[2]/input[1]').send_keys(str(company[i]))
        driver.find_element_by_xpath('//*[@id="module_frame"]/form[1]/table[3]/tbody/tr/td[1]/table/tbody/tr[6]/td[2]/input[1]').send_keys(str(address[i]))
        driver.find_element_by_xpath('//*[@id="module_frame"]/form[1]/table[3]/tbody/tr/td[1]/table/tbody/tr[7]/td[2]/input[1]').send_keys(str(zipcode[i]))
        driver.find_element_by_xpath('//*[@id="module_frame"]/form[1]/table[3]/tbody/tr/td[1]/table/tbody/tr[7]/td[2]/input[2]').send_keys(str(city[i]))
        driver.find_element_by_xpath('//*[@id="ext-gen31"]/img').click()
        driver.find_element_by_xpath('//*[@id="module_frame"]/form[1]/table[2]/tbody/tr/td[1]/table/tbody/tr/td[3]/button/img').click()
        driver.implicitly_wait(100)
        driver.find_element_by_xpath('//*[@id="module_frame"]/form[1]/table[3]/tbody/tr/td[1]/table/tbody/tr[1]/td[2]/div[2]/input').send_keys(str(system[i]))
        driver.find_element_by_xpath('//*[@id="ext-gen31"]/img').click()
        print("system is connected in system 1.")

        #copy voucher text and rights assign - working perfectly
        time.sleep(3)
        driver.find_element_by_xpath('//*[text()="brodos Distribution (1)"]').click()
        time.sleep(0.5)

        driver.find_element_by_xpath('//*[@id="ChangeSystemId"]').send_keys(str(system[i])+"\n")
        time.sleep(2)

        driver.get('https://www.brodos.net/index.php/mpath/admin_tools_copybillingtexts/')
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="submenu_table"]/tbody/tr[7]/td/a/span/span/span').click()
        driver.find_element_by_xpath('//*[@id="field-source-system"]').send_keys(str(333))
        driver.find_element_by_xpath('//*[@id="field-destination-system"]').send_keys(str(system[i]))
        driver.find_element_by_xpath('//*[@id="checkbox-overwrite"]').click()
        driver.find_element_by_xpath('//*[@id="ext-gen55"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ext-gen73"]').click()
        print(f"Voucher texts and assign rights are assigned to {str(system[i])}")

        #creating cross deb connection with system 1 - working perfectly
        driver.get('https://www.brodos.net/index.php/mpath/stamm_kre_create')
        driver.find_element_by_xpath('//*[@id="module_frame"]/form[1]/table[3]/tbody/tr/td[1]/table/tbody/tr[3]/td[2]/select/option[4]').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="module_frame"]/form[1]/table[3]/tbody/tr/td[1]/table/tbody/tr[1]/td[3]/input').send_keys(str(1))
        driver.find_element_by_xpath('//*[@id="module_frame"]/form[1]/table[3]/tbody/tr/td[1]/table/tbody/tr[4]/td[2]/input[1]').send_keys("Brodos AG")
        driver.find_element_by_xpath('//*[@id="module_frame"]/form[1]/table[3]/tbody/tr/td[1]/table/tbody/tr[6]/td[2]/input[1]').send_keys("Erlangen str")
        driver.find_element_by_xpath('//*[@id="module_frame"]/form[1]/table[3]/tbody/tr/td[1]/table/tbody/tr[6]/td[2]/input[2]').send_keys("9-13")
        driver.find_element_by_xpath('//*[@id="module_frame"]/form[1]/table[3]/tbody/tr/td[1]/table/tbody/tr[7]/td[2]/input[1]').send_keys('91083')
        driver.find_element_by_xpath('//*[@id="module_frame"]/form[1]/table[3]/tbody/tr/td[1]/table/tbody/tr[7]/td[2]/input[2]').send_keys("Baiersdorf")
        driver.find_element_by_xpath('//*[@id="module_frame"]/form[1]/table[5]/tbody/tr[1]/td[2]/table/tbody/tr[4]/td[2]/input').send_keys(str(customer[i]))
        driver.find_element_by_xpath('//*[@id="ext-gen31"]').click()
        print(f'Created a new supplier id in connection to system 1')

        #adding catalogue supplier
        driver.get('https://www.brodos.net/index.php/mpath/internaldata_dataoptions_distribconfiguration')
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="DISTRIBCONFIGURATIONVALUECATALOG_SUPPLIER"]').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="tbHeaderTable"]/tbody/tr[6]/td[4]/input').send_keys(str(1))
        driver.find_element_by_xpath('//*[@id="module_frame"]/form/table[2]/tbody/tr/td/table/tbody/tr/td[1]/button/img').click()
        print("Add catalogue supplier in the system")

        #Making the user connected with system
        time.sleep(3)
        driver.get('https://www.brodos.net/index.php/mpath/stamm_per_per')
        driver.find_element_by_xpath('//*[@id="ext-gen62"]').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="ext-gen132"]/div[1]/table/tbody/tr/td[2]/div').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="module_frame"]/form[1]/table[4]/tbody/tr/td/table/tbody/tr/td[7]').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="module_frame"]/form[1]/table[5]/tbody/tr/td/table/tbody/tr/td/button/img').click()
        driver.find_element_by_xpath('//*[@id="module_frame"]/form[1]/table[6]/tbody/tr[2]/td/button[1]').click()
        driver.find_element_by_xpath('//*[@id="module_frame"]/form[1]/table[5]/tbody/tr/td/table/tbody/tr/td[2]/button/img').click()
        driver.find_element_by_xpath('//*[@id="module_frame"]/form[1]/table[6]/tbody/tr[2]/td/button[1]').click()
        print("User is now connected with the system")

        #creating user with details csv rights
        driver.find_element_by_xpath('//*[@id="ext-gen25"]').click()
        time.sleep(0.5)
        driver.find_element_by_xpath('//*[text()="Own employees"]').click()
        time.sleep(0.5)
        driver.find_element_by_xpath('//*[@id="module_frame"]/form/table[2]/tbody/tr/td/table/tbody/tr/td[2]/button/img').click()
        time.sleep(0.5)
        driver.find_element_by_xpath('//*[@id="module_frame"]/form[1]/table[3]/tbody/tr/td[1]/table/tbody/tr[4]/td[2]/input').send_keys("import" + str(system[i]))
        driver.find_element_by_xpath('//*[@id="module_frame"]/form[1]/table[2]/tbody/tr/td/table/tbody/tr/td[1]/button/img').click()
        driver.implicitly_wait(20)
        driver.find_element_by_xpath('//*[@id="ext-gen59"]/b').click()
        driver.implicitly_wait(20)
        driver.find_element_by_xpath('//*[@id="ext-comp-1342"]').send_keys('marketplace-import@brodos.de')
        driver.find_element_by_xpath('//*[@id="ext-comp-1344"]').send_keys("import" + str(system[i]))
        driver.find_element_by_xpath('//*[@id="ext-gen156"]').click()
        driver.implicitly_wait(20)
        driver.find_element_by_xpath('//*[text()="customer-import via csv-file"]').click()
        driver.find_element_by_xpath('//*[@id="ext-gen51"]').click()
        print(f"User assigned with rights to add csv")
        driver.close()
        i += 1
        
        #Getting supplier-id
        driver.get('https://www.brodos.net/index.php/mpath/admin_access_distributor/')
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="ext-comp-1321"]').send_keys(str(system[i])+ "\n")
        supplier_id = int(driver.find_element_by_xpath('//*[@id="ext-gen46"]/div/table/tbody/tr/td[3]/div').text)
        supplier_id = supplier_id + 1
        print(f"Supplier id: {supplier_id}. I have added +1 in it, dont worry ;)")
        
except Exception as e:
    i += 1
    print(str(e))
    print('Sorry something went wrong while creation. Please attend manually from where its broken')

