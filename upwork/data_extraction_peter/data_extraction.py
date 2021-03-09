from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import json

from selenium.webdriver.support.wait import WebDriverWait

now = time.strftime("%H_%M_%S")


#Get the chrome driver according to your chrome version from here https://chromedriver.chromium.org/downloads
driver = webdriver.Chrome("E:/onlineshop images/onlineshop-support/res/chromedriver.exe") #set the path of the chrome driver

#Navigating to the scraping page
driver.get("http://arsiv.mackolik.com/Default.aspx")
driver.maximize_window()
driver.find_element_by_xpath('//*[@id="bottom-menu0"]/a[2]').click()
driver.implicitly_wait(30)

#navigating to league according to drop down list's index
selectleague = Select(driver.find_element_by_id("cboLeague"))
op1 = selectleague.options
for i in range(0, len(op1)):
    try:
        selectleague.select_by_index(i)
        driver.implicitly_wait(50)

        # navigating to season according to drop down list's index
        selectseason = Select(driver.find_element_by_id("cboSeason"))
        op2 = selectseason.options
        for j in range(0, len(op2)):
            selectseason.select_by_index(j)
            driver.implicitly_wait(50)
            driver.find_element_by_xpath('//*[@id="tab-list"]/li[3]/h2/a').click()
            # driver.find_element_by_xpath('//*[text()="Fikstür"]').click()    //this method can be used to search by text in webpage
            driver.implicitly_wait(50)

            # navigating to week according to drop down list's index
            selectweek = Select(driver.find_element_by_id("cboWeek"))
            op3 = selectweek.options
            for k in range(0, len(op3)):
                selectweek.select_by_index(k)
                # Looping through every match score
                table = driver.find_element_by_xpath('//*[@id="dvFixtureInner"]/table')
                wait = WebDriverWait(driver, 30)
                element = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/a[1]")))
                for row in table.find_elements_by_tag_name('tr')[1:]:
                    row = row.find_element_by_class_name("score")
                    row.click()
                    mainpage = driver.window_handles[0]
                    popup = driver.window_handles[1]
                    driver.switch_to.window(popup)
                    driver.implicitly_wait(5)
                    try:
                        #Meta details of match (saving details of the match)
                        team1 = driver.find_element_by_xpath('//*[@id="match-details"]/div/div[1]/div/div[2]/div[1]/div[1]/a').text
                        team2 = driver.find_element_by_xpath('//*[@id="match-details"]/div/div[1]/div/div[2]/div[3]/div[1]/a').text
                        ft = driver.find_element_by_xpath('//*[@id="dvScoreText"]').text
                        #creating a json file and appending data with every loop
                        with open(f"score{now}.json", 'a') as json_file:
                            dictionary = {"team1": team1, "team2": team2, "ft": ft}

                        json_file.write(json.dumps(dictionary))
                        json_file.close()
                        driver.close()
                        driver.switch_to.window(mainpage)
                    except Exception as e:
                        driver.close()
                        driver.switch_to.window(mainpage)
    except Exception as e:
        print(e)

