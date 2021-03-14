import time
from selenium import webdriver
import os
from dotenv import load_dotenv
load_dotenv()

import pandas as pd
# import xlrd

# get current page links
clientList = []

condition = True

# loop
while condition:
    try:
        print("try Block")
        df = pd.read_excel (r'./client.xls')
        clientList = df['Clients'].tolist()
        # condition = False
    except:
        print("except Block")
        condition = False
    finally:
        print("final block")

# driver.quit()