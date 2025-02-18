import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

web = "https://www.flipkart.com/search?q=makbook%20laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
path = r"C:\Users\Administrator\OneDrive\Documents\Data_Entry\PythonDOCS\chromedriver.exe"

service = Service (executable_path=path)

driver = webdriver.Chrome (service=service)

driver.get(web)
time.sleep(2)

titles = []
stars = []
ratting_reviews = []
discounts = []
prices = []

for i in range (3):
  title = driver.find_elements (By.XPATH,"(//div[@class='KzDlHZ'])")
  for t in title:
    titles.append(t.text)

star = driver.find_elements(By.XPATH,"(//div[@class='XQDdHH'])")
for s in star:
  stars.append(s.text)
  print(s.text)

ratting_review = driver.find_elements (By.XPATH,"(//span[@class='Wphh3N'])")
for r in ratting_review:
  ratting_reviews.append(r.text)

discount = driver.find_elements (By.XPATH,"(//div[@class='UkUFwK'])")
for d in discount:
  discounts.append(d.text)

price = driver.find_elements (By.XPATH,"(//div[@class='Nx9bqj _4b5DiR'])")
for p in price:
  prices.append(p.text)
wait = WebDriverWait(driver, 10)
next_button = driver.find_elements(By.XPATH,"(//a[@class='_9QVEpD'])")
next_button[0].click()
time.sleep(2)

min_len = min(len(titles),len(stars),len(ratting_reviews),len(discounts),len(prices))
titles = titles[:min_len]
stars = stars[:min_len]
ratting_reviews = ratting_reviews[:min_len]
discounts = discounts[:min_len]
prices = prices[:min_len]

df = pd.DataFrame({
    'Title': titles,
    'Stars': stars,
    'Ratting/Reviews': ratting_reviews,
    'Discounts': discounts,
    'Prices': prices})

print(df)

df.to_csv(r"C:\Users\Administrator\OneDrive\Documents\ApplePhones\MacbookLaptops.csv",index=False)