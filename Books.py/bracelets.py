import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

web="https://www.flipkart.com/jewellery/artificial-jewellery/bangles-bracelets-armlets/pr?sid=mcr,96v,fbc&p[]=facets.ideal_for%255B%255D%3DMen&p[]=facets.ideal_for%255B%255D%3DBoys&otracker=categorytree"
path=r"C:\Users\Administrator\OneDrive\Documents\Data_Entry\PythonDOCS\chromedriver.exe"

service=Service(executable_path=path)
driver=webdriver.Chrome(service=service)

driver.get(web)
time.sleep(2)

names=[]
titles=[]
old_prices=[]
discounts=[]
new_prices=[]

for i in range(1519):
  name=driver.find_elements(By.XPATH,"(//div[@class='syl9yP'])")
  title=driver.find_elements(By.XPATH,"(//a[@class='WKTcLC BwBZTg'])")
  old_price=driver.find_elements(By.XPATH,"(//div[@class='yRaY8j'])")
  discount=driver.find_elements(By.XPATH,"(//div[@class='UkUFwK'])")
  new_price=driver.find_elements(By.XPATH,"(//div[@class='Nx9bqj'])")

  for n in name:
    names.append(n.text)

  for t in title:
    titles.append(t.text)

  for old in old_price:
    old_prices.append(old.text)

  for d in discount:
    discounts.append(d.text)

  for new in new_price:
    new_prices.append(new.text)

next_button=driver.find_element(By.XPATH,"(//a[@class='_9QVEpD'])")
next_button.click()
time.sleep(2)

min_len=min(len(names),len(titles),len(old_prices),len(discounts),len(new_prices))
names=names[:min_len]
titles=titles[:min_len]
old_prices=old_prices[:min_len]
discounts=discounts[:min_len]
new_prices=new_prices[:min_len]

df=pd.DataFrame({'names':names,
                 'Titles':titles,
                 'Old prices':old_prices,
                 'Discounts':discounts,
                 'New prices':new_prices})

print(df)
