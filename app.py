import time
from selenium import webdriver
import os
from dotenv import load_dotenv
load_dotenv()

import pandas as pd

# constants
EMAIL = os.getenv("email")
PASSWORD = os.getenv("password")
BASEURL = 'https://www.linkedin.com/'
SEARCHURL = 'https://www.linkedin.com/search/results/people/?geoUrn=%5B%22103644278%22%5D&keywords=&origin=FACETED_SEARCH'
LOGINURL = BASEURL + 'uas/login/'
LOGINBTN = '//*[@id="organic-div"]/form/div[3]/button'
EMAILINPUT = 'username'
PASSWORDINPUT = 'password'
CONNECTBTN = 'pv-s-profile-actions--connect'
PROFILEBOX = 'pv-top-card'
CONNECTMODAL = "artdeco-modal-outlet"
NOTEBUTTON = 'artdeco-button--secondary'
NOTE = "We don't know each other. But, I saw your profile and we are sharing same fields of expertise did caught my interest. It would be my pleasure to make your acquaintance. Thanks for the connection."
NOTEBOX = 'custom-message'
CONNECTMODAL = "artdeco-modal-outlet"
SENDBUTTON = "artdeco-button--primary"
CANCELBUTTON = "artdeco-button--muted"
MODALCLOSEBUTTON = "artdeco-modal__dismiss"

# main code
# version 89 install driver based on the chrome version only
driver = webdriver.Chrome('./chromedriver.exe')
driver.get(LOGINURL)
email_box = driver.find_element_by_id(EMAILINPUT)
pass_box = driver.find_element_by_id(PASSWORDINPUT)
login_btn = driver.find_element_by_xpath(LOGINBTN)
email_box.send_keys(EMAIL)
pass_box.send_keys(PASSWORD)
login_btn.submit()
driver.maximize_window()

# get current page links
condition = True

# loop
while condition:
    print("try Block")
    df = pd.read_excel (r'./client.xls')
    clientList = df['Clients'].tolist()
    for el in clientList:
        driver.get(el)
        profileBox = driver.find_element_by_class_name(PROFILEBOX)
        connectBtn = profileBox.find_element_by_class_name(CONNECTBTN)
        disabled = True if connectBtn.get_attribute("disabled") else False
        if not disabled:
            checkText = connectBtn.find('artdeco-button__text').text
            checkTextAvail = True if checkText else False
            print(checkTextAvail)
            if checkTextAvail and checkText == 'Connect':
                connectBtn.click()
                modalBox = driver.find_element_by_id(CONNECTMODAL)
                opennoteBtn = modalBox.find_element_by_class_name(NOTEBUTTON)
                noteCheck = True if opennoteBtn else False
                if noteCheck:
                    opennoteBtn.click()
                    time.sleep(5)
                    addnotebox = modalBox.find_element_by_id(NOTEBOX)
                    addnotebox.send_keys(NOTE)
                    time.sleep(3)
                    sendBtn = modalBox.find_element_by_class_name(
                        SENDBUTTON)
                    closeBtn = modalBox.find_element_by_class_name(
                        MODALCLOSEBUTTON)
                    # check
                    senddisabled = True if sendBtn.get_attribute(
                        "disabled") else False
                    if not senddisabled:
                        sendBtn.click()
                    else:
                        closeBtn.click()
                else:
                    closeBtn.click()
            # end of block
        else:
            print("skipped")
    try:
        print("try Block")
    except:
        print("except Block")
        condition = False
    finally:
        print("final block")
        
# driver.quit()