import time
from bs4 import BeautifulSoup
from selenium import webdriver
import os
from dotenv import load_dotenv
load_dotenv()

# constants
EMAIL = os.getenv("email")
PASSWORD = os.getenv("password")
BASEURL = 'https://www.linkedin.com/'
LOGINURL = BASEURL + 'uas/login/'
SEARCHURL = 'https://www.linkedin.com/search/results/people/?geoUrn=%5B%22103644278%22%5D&keywords=medical%20billing%20owner&origin=FACETED_SEARCH&page=2'
EMAILINPUT = 'username'
PASSWORDINPUT = 'password'
LOGINBTN = '//*[@id="organic-div"]/form/div[3]/button'
SEARCHLISTCLASS = 'reusable-search__entity-results-list'
SEARCHLISTELEM = 'reusable-search__result-container'
NOTEBUTTON = 'artdeco-button--secondary'
NEXTBUTTON = 'artdeco-pagination__button--next'
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
driver.get(SEARCHURL)

# get current page links
condition = True
index = 1
successRequest = 0

def mainFunction():
    link = driver.find_elements_by_class_name(SEARCHLISTELEM)
    for el in link:
        connectBtn = el.find_element_by_tag_name('button')
        disabled = True if connectBtn.get_attribute("disabled") else False
        index += 1
        if not disabled:
            connectBtn.click()
            time.sleep(3)
            modalBox = driver.find_element_by_id(CONNECTMODAL)
            time.sleep(3)
            opennoteBtn = modalBox.find_element_by_class_name(NOTEBUTTON)
            opennoteBtn.click()
            time.sleep(5)
            addnotebox = modalBox.find_element_by_id(NOTEBOX)
            addnotebox.send_keys(NOTE)
            time.sleep(3)
            sendBtn = modalBox.find_element_by_class_name(SENDBUTTON)
            closeBtn = modalBox.find_element_by_class_name(MODALCLOSEBUTTON)
            # check
            senddisabled = True if sendBtn.get_attribute("disabled") else False
            if not senddisabled:
                sendBtn.click()
                successRequest += 1
            else:
                closeBtn.click()
            time.sleep(3)

def conditionCheck():
    if successRequest <= 50:
        if index == 10:
            index = 1
        mainFunction()
    else:
        print('Else Block')
        raise Exception("Loop exceeded 50 requests")
# loop
while condition:
    try:
        conditionCheck()
    except:
        print("except Block")
        condition = False
# driver.quit()
