import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

web = "https://www.flipkart.com/books/economics-business-and-management-books/finance-and-accounting-books/pr?sid=bks,xjk,n8m&otracker=categorytree"
path = r"C:\Users\Administrator\OneDrive\Documents\Data_Entry\PythonDOCS\chromedriver.exe"

service = Service (executable_path=path)
driver = webdriver.Chrome (service=service)

driver.get (web)
time.sleep(3)

titles = []
authors = []
stars = []
reviews = []
discounts = []
prices = []
for i in range (443):
  title = driver.find_elements (By.XPATH,"(//a[@class='wjcEIp'])")
  for t in title:
    titles.append (t.text)

  author = driver.find_elements (By.XPATH,"(//div[@class='NqpwHC'])")
  for a in author:
    authors.append (a.text)

  star = driver.find_elements (By.XPATH,"(//div[@class='XQDdHH'])")
  for s in star:
    stars.append (s.text)

  review = driver.find_elements (By.XPATH,"(//span[@class='Wphh3N'])")
  for r in review:
    reviews.append (r.text)

  discount = driver.find_elements (By.XPATH,"(//div[@class='UkUFwK'])")
  for d in discount:
    discounts.append(d.text)

  price = driver.find_elements (By.XPATH,"(//div[@class='UkUFwK'])")
  for p in price:
    prices.append(p.text)

next_button = driver.find_element (By.XPATH,"(//a[@class='_9QVEpD'])")
next_button.click()
time.sleep(3)

min_len = min(len(titles),len(stars),len(reviews),len(discounts),len(prices))
titles = titles [:min_len]
stars = stars [:min_len]
reviews = reviews [:min_len]
discounts = discounts [:min_len]
prices = prices [:min_len]

df = pd.DataFrame({'Titles':titles,
                   'Stars':stars,
                   'Reviews':reviews,
                   'Discounts':discounts,
                   'Prices':prices})

print(df)

df.to_csv(r"C:\Users\Administrator\OneDrive\Documents\Books\Finance & Accounting Books.csv",index=False)