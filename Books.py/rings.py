import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
web="https://www.flipkart.com/"
path=r"C:\Users\Administrator\OneDrive\Documents\Data_Entry\PythonDOCS\chromedriver.exe"
service=Service(executable_path=path)
driver=webdriver.Chrome(service=service)
driver.get(web)

input_element=driver.find_element(By.CLASS_NAME,"Pke_EE")
input_element.send_keys("Rings"+Keys.ENTER)
time.sleep(2)
names=[]
discounts=[]
prices=[]
for i in range(1693):
  name=driver.find_elements(By.XPATH,"(//div[@class='syl9yP'])")
  discount=driver.find_elements(By.XPATH,"(//div[@class='UkUFwK'])")
  price=driver.find_elements(By.XPATH,"(//div[@class='Nx9bqj'])")
  for n in name:
    names.append(n.text)
  for d in discount:
    discounts.append(d.text)
  for p in price:
    prices.append(p.text)
next_button=driver.find_element(By.XPATH,"(//a[@class='_9QVEpD'])")
next_button.click()
time.sleep(2)

df=pd.DataFrame({'Names':names,'Discounts':discounts,'Prices':prices})
print(df)

