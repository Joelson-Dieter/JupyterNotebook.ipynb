import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

web = "https://www.flipkart.com/food-products/pr?sid=eat&otracker=categorytree"
path = r"C:\Users\Administrator\OneDrive\Documents\Data_Entry\PythonDOCS\chromedriver.exe"

service = Service (executable_path=path)
driver = webdriver.Chrome (service = service)

driver.get (web)
time.sleep(5)

titles = []
stars = []
reviews = []
prices = []
measures = []

for i in range (291):
  title = driver.find_elements(By.XPATH,"(//a[@class='wjcEIp'])")
  for t in title:
    titles.append(t.text)

  star = driver.find_elements (By.XPATH,"(//div[@class='XQDdHH'])")
  for s in star:
    stars.append(s.text)

  review = driver.find_elements (By.XPATH,"(//span[@class='Wphh3N'])")
  for r in review:
    reviews.append (r.text)

  price = driver.find_elements (By.XPATH,"(//div[@class='Nx9bqj'])")
  for p in price:
    prices.append (p.text)

  measure = driver.find_elements (By.XPATH,"(//div[@class='NqpwHC'])")
  for m in measure:
    measures.append (m.text)

next_button = driver.find_element (By.XPATH,"(//a[@class='_9QVEpD'])")
next_button.click()
time.sleep (5)

min_len = min(len(titles),len(stars),len(reviews),len(prices),len(measures))
titles = titles [:min_len]
stars = stars [:min_len]
reviews = reviews [:min_len]
prices = prices [:min_len]
measures = measures [:min_len]

df=pd.DataFrame({'Titles':titles,'Stars':stars,'Reviews':reviews,'Prices':prices,'Measures':measures})

print(df)

df.to_csv (r"C:\Users\Administrator\OneDrive\Documents\Projects\Food Products.csv",index=False)