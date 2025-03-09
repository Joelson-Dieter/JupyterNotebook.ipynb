import time
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
web="https://www.flipkart.com/"
path=r"C:\Users\Administrator\OneDrive\Documents\Data_Entry\PythonDOCS\chromedriver.exe"
Service=Service(executable_path=path)
driver=webdriver.Chrome(service=Service)
driver.get(web)
input_element=driver.find_element(By.XPATH,"(//input[@class='Pke_EE'])")
input_element.send_keys("Umbrellas"+Keys.ENTER)
time.sleep(2)
titles=[]
colors=[]
stars=[]
reviews=[]
discounts=[]
old_prices=[]
new_prices=[]

for i in range(200):
  title=driver.find_elements(By.XPATH,"(//a[@class='wjcEIp'])")
  color=driver.find_elements(By.XPATH,"(//div[@class='NqpwHC'])")
  star=driver.find_elements(By.XPATH,"(//div[@class='XQDdHH'])")
  review=driver.find_elements(By.XPATH,"(//span[@class='Wphh3N'])")
  discount=driver.find_elements(By.XPATH,"(//div[@class='UkUFwK'])")
  old_price=driver.find_elements(By.XPATH,"(//div[@class='yRaY8j'])")
  new_price=driver.find_elements(By.XPATH,"(//div[@class='Nx9bqj'])")

  for t in title:
    titles.append(t.text)
  for c in color:
    colors.append(c.text)
  for s in star:
    stars.append(s.text)
  for rev in review:
    reviews.append(rev.text)
  for d in discount:
    discounts.append(d.text)
  for old in old_price:
    old_prices.append(old.text)
  for new in new_price:
    new_prices.append(new.text)

next_button=driver.find_element(By.CLASS_NAME,"_9QVEpD")
next_button.click()
time.sleep(2)

print(len(titles))
print(len(colors))
print(len(reviews))
print(len(discounts))
print(len(old_prices))
print(len(new_prices))

max_len=max(len(titles),len(colors),len(stars),len(reviews),len(discounts),len(old_prices),len(new_prices))
titles+=[np.nan]*(max_len-len(titles))
colors+=[np.nan]*(max_len-len(colors))
stars+=[np.nan]*(max_len-len(stars))
reviews+=[np.nan]*(max_len-len(reviews))
discounts+=[np.nan]*(max_len-len(discounts))
old_prices+=[np.nan]*(max_len-len(old_prices))
new_price+=[np.nan]*(max_len-len(new_prices))

df=pd.DataFrame({'Titles':titles,
                 'Colors':colors,
                 'Reviews':reviews,
                 'Discounts':discounts,
                 'Old prices':old_prices,
                 'New prices':new_prices})

print(df)

df.to_csv(r"C:\Users\Administrator\OneDrive\Documents\Projects\Umbrellas.csv",index=False)

pd.read_csv(r"C:\Users\Administrator\OneDrive\Documents\Projects\Umbrellas.csv")
print(df.head())