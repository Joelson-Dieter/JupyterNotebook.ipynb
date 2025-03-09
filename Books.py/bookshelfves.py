import time
import pandas as pd
import numpy as np
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
input_element.send_keys('Book shelf'+Keys.ENTER)
time.sleep(2)

titles=[]
colors=[]
stars=[]
reviews=[]
discounts=[]
prices=[]
for i in range(127):
  title=driver.find_elements(By.XPATH,"(//a[@class='wjcEIp'])")
  color=driver.find_elements(By.XPATH,"(//div[@class='NqpwHC'])")
  star=driver.find_elements(By.XPATH,"(//div[@class='XQDdHH'])")
  review=driver.find_elements(By.XPATH,"(//span[@class='Wphh3N'])")
  discount=driver.find_elements(By.XPATH,"(//div[@class='UkUFwK'])")
  price=driver.find_elements(By.XPATH,"(//div[@class='Nx9bqj'])")

  for t in title:
    titles.append(t.text)
  for c in color:
    colors.append(c.text)
  for s in star:
    stars.append(s.text)
  for r in review:
    reviews.append(r.text)
  for d in discount:
    discounts.append(d.text)
  for p in price:
    prices.append(p.text)

max_len=max(len(titles),len(colors),len(stars),len(reviews),len(discounts),len(prices))
titles+=[np.nan]*(max_len-len(titles))
colors+=[np.nan]*(max_len-len(colors))
stars+=[np.nan]*(max_len-len(stars))
reviews+=[np.nan]*(max_len-len(reviews))
discounts+=[np.nan]*(max_len-len(discounts))
prices+=[np.nan]*(max_len-len(prices))

df=pd.DataFrame({'Titles':titles,
                 'Colors':colors,
                 'Stars':stars,
                 'Reviews':reviews,
                 'Discounts':discounts,
                 'Prices':prices})

print(df)