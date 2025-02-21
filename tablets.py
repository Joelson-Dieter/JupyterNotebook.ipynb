import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

web = "https://www.flipkart.com/search?q=tablets&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
path = r"C:\Users\Administrator\OneDrive\Documents\Data_Entry\PythonDOCS\chromedriver.exe"

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)

driver.get(web)
time.sleep(2)

titles = []
stars = []
reviews = []
discounts = []
prices = []

for i in range (46):
  title = driver.find_elements(By.XPATH,"(//div[@class='KzDlHZ'])")
  for t in title:
    titles.append(t.text)

  star = driver.find_elements (By.XPATH,"(//div[@class='XQDdHH'])")
  for s in star:
    stars.append (s.text)

  review = driver.find_elements (By.XPATH,"(//span[@class='Wphh3N'])")
  for r in review:
    reviews.append(r.text)

  discount = driver.find_elements(By.XPATH,"(//div[@class='UkUFwK'])")
  for d in discount:
    discounts.append(d.text)

  price = driver.find_elements (By.XPATH,"(//div[@class='Nx9bqj _4b5DiR'])")
  for p in price:
    prices.append(p.text)

next_button = driver.find_element(By.XPATH,"(//a[@class='_9QVEpD'])")
next_button.click()
time.sleep(2)

min_len = min(len(titles),len(stars),len(reviews),len(discounts),len(prices))
titles = titles [:min_len]
stars = stars [:min_len]
reviews = reviews [:min_len]
discounts = discounts [:min_len]
prices = prices [:min_len]

df=pd.DataFrame({'Titles':titles,'Stars':stars,'Reviews':reviews,'Discounts':discounts,'Prices':prices})
print(df)

df.to_csv (r"C:\Users\Administrator\OneDrive\Documents\ApplePhones\Tablets.csv",index=False)