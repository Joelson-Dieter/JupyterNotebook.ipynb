import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

web="https://www.flipkart.com/bags-wallets-belts/belts/pr?sid=reh,ro3&otracker=categorytree"
path=r"C:\Users\Administrator\OneDrive\Documents\Data_Entry\PythonDOCS\chromedriver.exe"

service=Service(executable_path=path)
driver=webdriver.Chrome(service=service)

driver.get(web)
time.sleep(2)
names=[]
old_prices=[]
discounts=[]
new_prices=[]
for i in range(1517):
  name=driver.find_elements(By.XPATH,"(//div[@class='syl9yP'])")
  old_price=driver.find_elements(By.XPATH,"(//div[@class='yRaY8j'])")
  discount=driver.find_elements(By.XPATH,"(//div[@class='UkUFwK'])")
  new_price=driver.find_elements(By.XPATH,"(//div[@class='Nx9bqj'])")

  for n in name:
    names.append(n.text)
  for old in old_price:
    old_prices.append(old.text)
  for d in discount:
    discounts.append(d.text)
  for new in new_price:
    new_prices.append(new.text)

next_button=driver.find_element(By.XPATH,"(//a[@class='_9QVEpD'])")
next_button.click()
time.sleep(2)

df=pd.DataFrame({'Names':names,'Old price':old_prices,'Discounts':discounts,'New_prices':new_prices})
print(df)

df.to_csv(r"C:\Users\Administrator\OneDrive\Documents\Projects\Belts.csv",index=False)
