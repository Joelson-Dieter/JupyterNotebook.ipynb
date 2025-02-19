import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

web = "https://www.flipkart.com/"
path = r"C:\Users\Administrator\OneDrive\Documents\Data_Entry\PythonDOCS\chromedriver.exe"

service = Service(executable_path=path)

driver = webdriver.Chrome(service=service)

driver.get(web)

time.sleep(2)

input_search = driver.find_elements (By.XPATH,"(//div[@class='_2SmNnR'])")

search_button = driver.find_elements (By.XPATH,"(//button[@class='_2iLD__'])")

input_search[0].send_keys("Electronics")

search_button[0].click()
time.sleep(2)

