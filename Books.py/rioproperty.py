import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
web="https://www.riocan.com/English/our-properties/leasing/all-properties/"
path=r"C:\Users\Administrator\OneDrive\Documents\Data_Entry\PythonDOCS\chromedriver.exe"
service=Service(executable_path=path)
driver=webdriver.Chrome(service=service)
driver.get(web)
time.sleep(2)
property=driver.find_elements(By.XPATH,"//a[@href='/English/our-properties/leasing/details/2016/1293-Bloor-Street-West/default.aspx' and contains(text(), '1293 Bloor Street West')]")
for p in property:
  print(p.text)