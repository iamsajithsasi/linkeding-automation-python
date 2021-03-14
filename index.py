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
inputText = input("Enter search text:- ")
searchText = inputText.strip()
newText = searchText.replace(" ", "%20").lower()
SEARCHURL = 'https://www.linkedin.com/search/results/people/?geoUrn=%5B%22103644278%22%5D&keywords='+newText+'&origin=FACETED_SEARCH'
EMAILINPUT = 'username'
PASSWORDINPUT = 'password'
LOGINBTN = '//*[@id="organic-div"]/form/div[3]/button'
SEARCHLISTCLASS = 'reusable-search__entity-results-list'
SEARCHLISTELEM = 'reusable-search__result-container'
NOTEBUTTON = 'artdeco-button--secondary'
PAGINATIONBOX = 'artdeco-pagination'
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
index = 1
successRequest = 0
pageNo = 2

# loop
while condition:
    print("within main")
    link = driver.find_elements_by_class_name(SEARCHLISTELEM)
    for el in link:
        connectBtn = el.find_element_by_tag_name('button')
        disabled = True if connectBtn.get_attribute("disabled") else False
        if not disabled:
            print("connect ", el.find_element_by_class_name(
                'app-aware-link').get_property('href'))
            checkText = connectBtn.find_element_by_class_name(
                'artdeco-button__text').text
            # print("checkText", checkText)
            if checkText == 'Connect':
                driver.execute_script("arguments[0].click();", connectBtn)
                time.sleep(3)
                modalCheck = True if driver.find_element_by_id(
                    CONNECTMODAL) else False
                if modalCheck:
                    modalBox = driver.find_element_by_id(CONNECTMODAL)
                    time.sleep(3)
                    opennoteBtn = modalBox.find_element_by_class_name(
                        NOTEBUTTON)
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
                            successRequest += 1
                        else:
                            closeBtn.click()
                    else:
                        closeBtn.click()
                    # end of block
                time.sleep(3)
            elif checkText == 'Follow':
                connectBtn.click()
            else:
                print("skip", checkText)
        else:
            print("pend ", el.find_element_by_class_name(
                'app-aware-link').get_property('href'))
        index += 1
    try:
        pageNo += 1
        print("try Block")
    except:
        print("except Block")
        condition = False
    else:
        print("else block")
    finally:
        print("final block")
        time.sleep(5)
        if successRequest <= 50:
            driver.get(SEARCHURL + '&page=' + str(pageNo))  # switch to window
            # time.sleep(10)
            # pageBox = driver.find_element_by_class_name(PAGINATIONBOX)
            # nextBtn = pageBox.find_element_by_class_name(NEXTBUTTON)
            # # driver.execute_script("arguments[0].scrollIntoView();", nextBtn)
            # driver.execute_script("arguments[0].click();", nextBtn)
            time.sleep(10)
        else:
            condition = False
# driver.quit()
