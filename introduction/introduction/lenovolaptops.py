import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

web = "https://www.flipkart.com/search?q=lenovo%20laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
path = r"C:\Users\Administrator\OneDrive\Documents\Data_Entry\PythonDOCS\chromedriver.exe"

service = Service(executable_path=path)
driver = webdriver.Chrome (service=service)

driver.get (web)
time.sleep(2)

titles = []
prices = []

for i in range (16):
  title = driver.find_elements(By.XPATH,"(//div[@class='KzDlHZ'])")
  for t in title:
    titles.append(t.text)

  price = driver.find_elements(By.XPATH,"(//div[@class='Nx9bqj _4b5DiR'])")
  for p in price:
    prices.append(p.text)

next_button = driver.find_element(By.XPATH,"(//a[@class='_9QVEpD'])")
next_button.click()
time.sleep(2)

df = pd.DataFrame({'Titles':titles,'Prices':prices})

print(df)

df.to_csv(r"C:\Users\Administrator\OneDrive\Documents\ApplePhones\LenovoLaptops.csv",index=False)