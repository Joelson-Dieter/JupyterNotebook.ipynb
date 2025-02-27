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
input_element=driver.find_element(By.XPATH,"(//input[@class='Pke_EE'])")
input_element.send_keys("Kids shorts"+Keys.ENTER)
time.sleep(3)

names=[]
colors=[]
old_prices=[]
discounts=[]
new_prices=[]
for i in range(255):
  name=driver.find_elements(By.XPATH,"(//div[@class='syl9yP'])")
  color=driver.find_elements(By.XPATH,"(//div[@class='Br9IW+'])")
  old_price=driver.find_elements(By.XPATH,"(//div[@class='yRaY8j'])")
  discount=driver.find_elements(By.XPATH,"(//div[@class='UkUFwK'])")
  new_price=driver.find_elements(By.XPATH,"(//div[@class='Nx9bqj'])")
  for n in name:
    names.append(n.text)
  for c in color:
    colors.append(c.text)
  for old in old_price:
    old_prices.append(old.text)
  for d in discount:
    discounts.append(d.text)
  for new in new_price:
    new_prices.append(new.text)
next_button=driver.find_element(By.XPATH,"(//a[@class='_9QVEpD'])")
next_button.click()
time.sleep(3)
min_len=min(len(names),len(colors),len(old_prices),len(discounts),len(new_prices))
names=names[:min_len]
colors=colors[:min_len]
old_prices=new_prices[:min_len]
discounts=discounts[:min_len]
new_prices=new_prices[:min_len]
df=pd.DataFrame({'Names':names,'Colors':colors,'old price':old_prices,'Discounts':discounts,'New prices':new_prices})
print(df)

df.to_csv(r"C:\Users\Administrator\OneDrive\Documents\Projects\Kids shorts.csv",index=False)

                          
