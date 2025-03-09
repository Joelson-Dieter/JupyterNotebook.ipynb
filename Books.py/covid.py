import time
import pandas as pd
from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
web="https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"
path=r"C:\Users\Administrator\OneDrive\Documents\Data_Entry\PythonDOCS\chromedriver.exe"
service=Service(executable_path=path)
driver=webdriver.Chrome(service=service)
driver.get(web)
time.sleep(5)
countries=[]
country=driver.find_elements(By.XPATH,"//a[contains(text(), 'GDP') or contains(@href, 'GDP')]")
estimate=driver.find_elements(By.XPATH,"(//tbody/tr/td[4])")
for i in estimate:
  print(i.text)
