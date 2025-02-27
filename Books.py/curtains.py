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
input_element.send_keys('Curtains & Accessories'+Keys.ENTER)

time.sleep(3)

titles=[]
packs_of=[]
stars=[]
reviews=[]
discounts=[]
prices=[]

for i in range(253):
  title=driver.find_elements(By.XPATH,"(//a[@class='wjcEIp'])")
  pack_of=driver.find_elements(By.XPATH,"(//div[@class='NqpwHC'])")
  star=driver.find_elements(By.XPATH,"(//div[@class='XQDdHH'])")
  review=driver.find_elements(By.XPATH,"(//span[@class='Wphh3N'])")
  discount=driver.find_elements(By.XPATH,"(//div[@class='UkUFwK'])")
  price=driver.find_elements(By.XPATH,"(//div[@class='Nx9bqj'])")

  for t in title:
    titles.append(t.text)
  for pack in pack_of:
    packs_of.append(pack.text)
  for s in star:
    stars.append(s.text)
  for r in review:
    reviews.append(r.text)
  for d in discount:
    discounts.append(d.text)
  for p in price:
    prices.append(p.text)
next_button=driver.find_element(By.CLASS_NAME,"_9QVEpD")
next_button.click()

time.sleep(3)

min_len=min(len(titles),len(packs_of),len(stars),len(reviews),len(discounts),len(prices))
titles=titles[:min_len]
packs_of=packs_of[:min_len]
stars=stars[:min_len]
reviews=reviews[:min_len]
discounts=discounts[:min_len]
prices=prices[:min_len]

df=pd.DataFrame({'Titles':titles,'Packs in':packs_of,'Stars':stars,'Reviews':reviews,'Discounts':discounts,'Prices':prices})

print(df)
df.to_csv(r"C:\Users\Administrator\OneDrive\Documents\Projects\Curtains&Accessories.csv",index=False)