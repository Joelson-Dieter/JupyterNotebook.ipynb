import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

web = "https://yellow.co.ke/categories/computer-equipment"
path = r"C:\Users\Administrator\OneDrive\Documents\Data_Entry\PythonDOCS\chromedriver.exe"

service = Service(executable_path=path)
driver = webdriver.Chrome (service=service)

driver.get (web)
time.sleep(2)

company_names = []
shipments = []
addresses = []

for i in range (2):

  company_name = driver.find_elements(By.XPATH,"(//h4[@class='title'])")
  shipment = driver.find_elements(By.TAG_NAME,"p")
  address = driver.find_elements(By.XPATH,"(//div[@class='address-details'])")


  for company in company_name:
    company_names.append(company.text)

  for ship in shipment:
    shipments.append(ship.text)

  for add in address:
    addresses.append(add.text)

  next_button = driver.find_element(By.TAG_NAME,'a')
  next_button.click()
print(len(company_names))
print(len(shipments))
print(len(addresses))