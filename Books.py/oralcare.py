import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

web = "https://www.flipkart.com/beauty-and-grooming/oral-care/pr?sid=g9b,cey&otracker=categorytree"
path = r"C:\Users\Administrator\OneDrive\Documents\Data_Entry\PythonDOCS\chromedriver.exe"

service = Service(executable_path=path)
driver = webdriver.Chrome (service=service)

driver.get(web)
time.sleep(2)

titles=[]
capacities=[]
stars=[]
reviews=[]
discounts=[]
prices=[]
comments=[]

for i in range(1,535):

  title = driver.find_elements(By.XPATH,"(//a[@class='wjcEIp'])")
  capacity = driver.find_elements(By.XPATH,"(//div[@class='NqpwHC'])")
  star = driver.find_elements(By.XPATH,"(//div[@class='XQDdHH'])")
  review = driver.find_elements(By.XPATH,"(//span[@class='Wphh3N'])")
  discount = driver.find_elements(By.XPATH,"(//div[@class='UkUFwK'])")
  price = driver.find_elements(By.XPATH,"(//div[@class='Nx9bqj'])")
  comment = driver.find_elements(By.XPATH,"(//div[@class='yiggsN O5Fpg8'])")

  for t in title:
    titles.append(t.text)

  for c in capacity:
    capacities.append(c.text)

  for s in star:
    stars.append(s.text)

  for r in review:
    reviews.append(r.text)

  for d in discount:
    discounts.append(d.text)

  for p in price:
    prices.append(p.text)

  for com in comment:
    comments.append(com.text)

next_button=driver.find_element(By.CLASS_NAME,"_9QVEpD")
next_button.click()
time.sleep(2)

min_len=min(len(titles),len(capacities),len(stars),len(reviews),len(discounts),len(prices),len(comments))
titles=titles[:min_len]
capacities=capacities[:min_len]
stars=stars[:min_len]
reviews=reviews[:min_len]
discounts=discounts[:min_len]
prices=prices[:min_len]
comments=comments[:min_len]

df=pd.DataFrame({'Titles':titles,
                 'Capacities':capacities,
                 'Stars':stars,
                 'Reviews':reviews,
                 'Discounts':discounts,
                 'Prices':prices,
                 'Comments':comments})

print(df)

df.to_csv(r"C:\Users\Administrator\OneDrive\Documents\Projects\Oralcare.csv",index=False)



