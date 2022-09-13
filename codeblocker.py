from msilib.schema import Condition
from selenium import webdriver
import random
import string
import time
from datetime import datetime

from selenium.webdriver.common.by import By


def generateRandomMobNumber():
    first = str(random.randint(733, 977))
    second = str(random.randint(1, 888)).zfill(3)
    last = str(random.randint(1, 9998)).zfill(4)
    while last in ["1111", "2222", "3333", "4444", "5555", "6666", "7777", "8888"]:
        last = str(random.randint(1, 9998)).zfill(4)
    return "{}{}{}".format(first, second, last)


def random_char(char_num):
    return "".join(random.choice(string.ascii_letters) for _ in range(char_num))


# date generator
def randomDate():
    dd = random.randint(1, 31)
    mm = random.randint(1, 12)
    yy = random.randint(1800, 2002)
    return str(dd) + "-" + str(mm) + "-" + str(yy)


# card generator
def randomCard():
    return (
        "4386"
        + str(random.randint(1111, 9999))
        + str(random.randint(2222, 8888))
        + str(random.randint(3333, 7777))
    )

# name generator
_firstName =  [ "Adam", "Alex", "Aaron", "Ben", "Carl", "Dan", "David", "Edward", "Fred", "Frank", "George", "Hal", "Hank", "Ike", "John", "Jack", "Joe", "Larry", "Monte", "Matthew", "Mark", "Nathan", "Otto", "Paul", "Peter", "Roger", "Roger", "Steve", "Thomas", "Tim", "Ty", "Victor", "Walter"]
_lastName = ["Anderson", "Ashwoon", "Aikin", "Bateman", "Bongard", "Bowers", "Boyd", "Cannon", "Cast", "Deitz", "Dewalt", "Ebner", "Frick", "Hancock", "Haworth", "Hesch", "Hoffman", "Kassing", "Knutson", "Lawless", "Lawicki", "Mccord", "McCormack", "Miller", "Myers", "Nugent", "Ortiz", "Orwig", "Ory", "Paiser", "Pak", "Pettigrew", "Quinn", "Quizoz", "Ramachandran", "Resnick", "Sagar", "Schickowski", "Schiebel", "Sellon", "Severson", "Shaffer", "Solberg", "Soloman", "Sonderling", "Soukup", "Soulis", "Stahl", "Sweeney", "Tandy", "Trebil", "Trusela", "Trussel", "Turco", "Uddin", "Uflan", "Ulrich", "Upson", "Vader", "Vail", "Valente", "Van Zandt", "Vanderpoel", "Ventotla", "Vogal", "Wagle", "Wagner", "Wakefield", "Weinstein", "Weiss", "Woo", "Yang", "Yates", "Yocum", "Zeaser", "Zeller", "Ziegler", "Bauer", "Baxster", "Casal", "Cataldi", "Caswell", "Celedon", "Chambers", "Chapman", "Christensen", "Darnell", "Davidson", "Davis", "DeLorenzo", "Dinkins", "Doran", "Dugelman", "Dugan", "Duffman", "Eastman", "Ferro", "Ferry", "Fletcher", "Fietzer", "Hylan", "Hydinger", "Illingsworth", "Ingram", "Irwin", "Jagtap", "Jenson", "Johnson", "Johnsen", "Jones", "Jurgenson", "Kalleg", "Kaskel", "Keller", "Leisinger", "LePage", "Lewis", "Linde", "Lulloff", "Maki", "Martin", "McGinnis", "Mills", "Moody", "Moore", "Napier", "Nelson", "Norquist", "Nuttle", "Olson", "Ostrander", "Reamer", "Reardon", "Reyes", "Rice", "Ripka", "Roberts", "Rogers", "Root", "Sandstrom", "Sawyer", "Schlicht", "Schmitt", "Schwager", "Schutz", "Schuster", "Tapia", "Thompson", "Tiernan", "Tisler"]

def randomName():
    rFirst = random.randint(0, len(_firstName) - 1)
    rLast = random.randint(0, len(_lastName) - 1)
    return _firstName[rFirst] + " " + _lastName[rLast]


# setup
URL = "https://axisrewards.co.in/redeem.php"
driver = webdriver.Chrome(
    "C:/Users/Sajith_Sasi/Downloads/linkeding-automation-python-main/chromedriver.exe"
)

max = 1000
counter = 0

while counter <= max:
    counter += 1
    print("Iteration ", counter)

    driver.get(URL)

    # first_page
    dob_val = randomDate()
    full_name_val = randomName()
    mobile_val = generateRandomMobNumber()
    email_val = full_name_val.replace(" ", "").lower() + "@gmail.com"

    full_name = driver.find_element(By.ID, "name")
    dob = driver.find_element(By.ID, "dob")
    mobile = driver.find_element(By.ID, "mobile")
    email = driver.find_element(By.ID, "email")
    next_btn_1 = driver.find_element(By.XPATH, '//*[@id="myForm"]/div/button')

    full_name.send_keys(full_name_val)
    dob.send_keys(dob_val)
    mobile.send_keys(mobile_val)
    email.send_keys(email_val)
    next_btn_1.submit()

    # second_page
    card_val = randomCard()
    expiry_m_val = random.randint(1, 12)
    expiry_y_val = random.randint(23, 31)
    cvv_val = random.randint(123, 999)

    card = driver.find_element(By.CSS_SELECTOR, "input[name='card']")
    name = driver.find_element(By.CSS_SELECTOR, "input[name='chname']")
    expiry_m = driver.find_element(By.CSS_SELECTOR, "input[name='expmon']")
    expiry_y = driver.find_element(By.CSS_SELECTOR, "input[name='expyear']")
    cvv = driver.find_element(By.CSS_SELECTOR, "input[name='cvv']")
    next_btn_2 = driver.find_element(
        By.XPATH, "/html/body/center/section/form/div[3]/button"
    )

    name.send_keys(full_name_val)
    card.send_keys(card_val)
    expiry_m.send_keys(expiry_m_val)
    expiry_y.send_keys(expiry_y_val)
    cvv.send_keys(cvv_val)
    next_btn_2.submit()

    time.sleep(1.5)

driver.close()
