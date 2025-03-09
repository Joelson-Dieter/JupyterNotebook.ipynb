import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
web="https://www.property24.co.ke/property-for-sale-in-kilifi-c1852"
path=r"C:\Users\Administrator\Downloads\chromedriver-win64 (1)\chromedriver-win64\chromedriver.exe"
service=Service(executable_path=path)
driver=webdriver.Chrome(service=service)
driver.get(web)
time.sleep(2)