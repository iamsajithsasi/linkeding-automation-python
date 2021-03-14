import time
from bs4 import BeautifulSoup
from selenium import webdriver
import os
from dotenv import load_dotenv
load_dotenv()

import pandas as pd

# constants
EMAIL = os.getenv("email")
PASSWORD = os.getenv("password")
BASEURL = 'https://www.linkedin.com/'
LOGINURL = BASEURL + 'uas/login/'
SEARCHURL = 'https://www.linkedin.com/search/results/people/?geoUrn=%5B%22103644278%22%5D&keywords=medical%20billing%20owner&origin=FACETED_SEARCH&page=3'
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
driver.maximize_window()
driver.get(SEARCHURL)

# get current page links
condition = True
listoflinks = []

# loop
while condition:
    link = driver.find_elements_by_class_name(SEARCHLISTELEM)
    for el in link:
        connectBtn = el.find_element_by_tag_name('button')
        disabled = True if connectBtn.get_attribute("disabled") else False
        if not disabled:
            atag = el.find_element_by_class_name('app-aware-link').get_property('href')
            listoflinks.append(atag)
    try:
        print("try Block")
    except:
        condition = False
    finally:
        linkstable = pd.DataFrame(listoflinks)
        linkstable.rename(index=str, columns={0:'new_column_name'})
        linkstable.to_csv('list.csv')
# driver.quit()