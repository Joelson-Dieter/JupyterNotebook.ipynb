import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

web = "https://www.flipkart.com/search?q=infinix&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
path = r"C:\Users\Administrator\OneDrive\Documents\Data_Entry\PythonDOCS\chromedriver.exe"

service = Service (executable_path=path)
driver = webdriver.Chrome (service=service)

driver.get(web)
time.sleep(10)

titles = []
stars = []
reviews = []
old_prices = []
discounts = []
new_prices = []

for i in range (1853):

  title = driver.find_elements (By.XPATH,"(//a[@class='wjcEIp'])")
  for t in title:
    titles.append(t.text)
  
  star = driver.find_elements (By.XPATH,"(//div[@class='XQDdHH'])")
  for s in star:
    stars.append(s.text)
  
  review = driver.find_elements(By.XPATH,"(//span[@class='Wphh3N'])")
  for rev in review:
    reviews.append(rev.text)
  
  old_price = driver.find_elements(By.XPATH,"(//div[@class='yRaY8j'])")
  for old in old_price:
    old_prices.append(old.text)
  
  discount = driver.find_elements(By.XPATH,"(//div[@class='UkUFwK'])")
  for d in discount:
    discounts.append(d.text)
  
  new_price = driver.find_elements(By.XPATH,"(//div[@class='Nx9bqj'])")
  for new in new_price:
    new_prices.append(new.text)
  
  next_button = driver.find_element(By.XPATH,"(//a[@class='_9QVEpD'])")
  next_button.click()
  time.sleep(10)

  min_len = min(len(titles),len(star),len(reviews),len(old_prices),len(discounts),len(new_prices))
  titles = titles[:min_len]
  stars = stars[:min_len]
  reviews = reviews[:min_len]
  old_prices = old_prices[:min_len]
  discounts = discounts[:min_len]
  new_prices = new_prices[:min_len]

  df = pd.DataFrame({'Titles':titles,'Stars':stars, 'Reviews':reviews, 'Old Price':old_prices, 'Discounts':discounts, 'New Price':new_prices})

  print(df)

  df.to_csv(r"C:\Users\Administrator\OneDrive\Documents\ApplePhones\flipkartnfinixPhones.csv",index=False)
  