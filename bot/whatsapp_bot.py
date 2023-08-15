#Value of Expected Elapsed Time is considered double of generally expected Elapsed Time, due to time.sleep() usage across the utility
#Test : Bot should be able to send a message to the receiver user within decided time constraint, else we mark it as fail

import sys
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def user_chat(user_name,message):

    try:
        search_bar = driver.find_element(By.CSS_SELECTOR,'.selectable-text.copyable-text.iq0m558w.g0rxnol2')
        time.sleep(2)
        search_bar.click()
        time.sleep(2)

        #check whether username exists in WhatsApp contact list or not
        try:
            search_bar.send_keys(user_name)
            time.sleep(3)
            driver.find_element(By.XPATH,"//span[@title='{0}']".format(user_name)).click()
            time.sleep(3)
        except:
            print("User Name {0} Not Found In Contacts List".format(user_name))
            return

        text_bar = driver.find_element(By.XPATH, "//div/div[@class='_3Uu1_']")
        time.sleep(3)
        text_bar.click()
        time.sleep(3)
        text_bar.send_keys("INCOMING MESSAGE FOR USER : {0}\n{1}".format(user_name,message))
        time.sleep(3)
        driver.find_element(By.XPATH, "//span[@data-testid='send']").click()
        time.sleep(3)
    except Exception as e:
        l = str(e).split(';')
        print("Error : {0}".format(l[0]))
        return

if __name__=='__main__':

    receiver_names = sys.argv[1]
    message = sys.argv[2]
    my_options = webdriver.ChromeOptions()
    service_obj = Service("INSERT FILE LOCATION FOR chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj, options=my_options)
    driver.get("https://web.whatsapp.com/")
    driver.implicitly_wait(15)
    # wait until QR code presence is located in the webpage
    wait = WebDriverWait(driver, 15)
    wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "._10aH-")))
    time.sleep(20)
    name_list = receiver_names.split(',')
    for name in name_list:
        event_start_time = datetime.now().replace(microsecond=0)
        user_chat(name,message)
        event_end_time = datetime.now().replace(microsecond=0)
        elapsed_time = event_end_time-event_start_time
        print("Expected Elapsed Time for {0} : 0:00:30".format(name))
        print("Observed Elapsed Time for {0} : {1}".format(name,elapsed_time))
        driver.refresh()

    driver.close()
