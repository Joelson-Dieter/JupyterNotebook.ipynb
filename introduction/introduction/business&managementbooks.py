import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

web = "https://www.flipkart.com/books/economics-business-and-management-books/business-and-management-books/pr?sid=bks,xjk,cyn&otracker=categorytreer"
path = r"C:\Users\Administrator\OneDrive\Documents\Data_Entry\PythonDOCS\chromedriver.exe"

service = Service(executable_path=path)
driver = webdriver.Chrome (service=service)

driver.get (web)
time.sleep (2)

titles = []
authors = []
stars = []
reviews = []
discounts = []
prices = []

for i in range (491):
  title = driver.find_elements (By.XPATH,"(//a[@class='wjcEIp'])")
  for t in title:
    titles.append(t.text)

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
    prices.append (p.text)

next_button = driver.find_element (By.XPATH,"(//a[@class='_9QVEpD'])")
next_button.click()
time.sleep(2)

min_len = min(len(titles),len(authors),len(stars),len(reviews),len(discounts),len(prices))
titles = titles [:min_len]
authors = authors [:min_len]
stars = stars [:min_len]
reviews = reviews [:min_len]
discounts = discounts [:min_len]
prices = prices [:min_len]

df = pd.DataFrame({'Titles':titles,
                    'Authors':authors,
                    'Stars':stars,
                    'Reviews':reviews,
                    'Discounts':discounts,
                    'Prices':prices})
  
print(df)

df.to_csv (r"C:\Users\Administrator\OneDrive\Documents\Books\Business & Management Books.csv",index=False)