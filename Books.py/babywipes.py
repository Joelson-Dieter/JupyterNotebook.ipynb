import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
web="https://www.flipkart.com/"
path=r"C:\Users\Administrator\OneDrive\Documents\Data_Entry\PythonDOCS\chromedriver.exe"
Service=Service(executable_path=path)
driver=webdriver.Chrome(service=Service)
driver.get(web)
input_element=driver.find_element(By.CLASS_NAME,"Pke_EE")
time.sleep(2)
titles=[]
pieces=[]
stars=[]
reviews=[]
discounts=[]
prices=[]
for i in range (52):
  title=driver.find_elements(By.XPATH,"(//a[@class='wjcEIp'])")
  piece=driver.find_elements(By.XPATH,"(//div[@class='NqpwHC'])")
  star=driver.find_elements(By.XPATH,"(//div[@class='XQDdHH'])")
  review=driver.find_elements(By.XPATH,"(//span[@class='Wphh3N'])")
  discount=driver.find_elements(By.XPATH,"(//div[@class='UkUFwK'])")
  price=driver.find_elements(By.XPATH,"(//div[@class='Nx9bqj'])")

  for t in title:
    titles.append(t.text)
  for pc in piece:
    pieces.append(pc.text)
  for s in star:
    stars.append(s.text)
  for r in review:
    reviews.append(r.text)
  for d in discount:
    discounts.append(d.text)
  for p in price:
    prices.append(p.text)
next_button=driver.find_element(By.XPATH,"(//a[@class='_9QVEpD'])")
next_button.click()
time.sleep(2)
min_len=min(len(titles),len(pieces),len(stars),len(reviews),len(discounts),len(prices))
titles=titles[:min_len]
pieces=pieces[:min_len]
stars=stars[:min_len]
reviews=reviews[:min_len]
discounts=discounts[:min_len]
prices=prices[:min_len]

df=pd.DataFrame({'Titles':titles,
                 'Pieces':pieces,
                 'Stars':stars,
                 'Reviews':reviews,
                 'Discounts':discounts,
                 'Prices':prices
                 
                 })
print(df)
df.to_csv(r"C:\Users\Administrator\OneDrive\Documents\Projects\Babywipes.csv",index=False)