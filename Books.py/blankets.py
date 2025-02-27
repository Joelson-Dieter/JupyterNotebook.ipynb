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
input_element.send_keys("Blankets"+Keys.ENTER)
time.sleep(5)

titles=[]
colors=[]
stars=[]
reviews=[]
old_prices=[]
discounts=[]
new_prices=[]
for i in range(283):

  title=driver.find_elements(By.XPATH,"(//a[@class='wjcEIp'])")
  color=driver.find_elements(By.XPATH,"(//div[@class='NqpwHC'])")
  star=driver.find_elements(By.XPATH,"(//div[@class='XQDdHH'])")
  review=driver.find_elements(By.XPATH,"(//span[@class='Wphh3N'])")
  old_price=driver.find_elements(By.XPATH,"(//div[@class='yRaY8j'])")
  discount=driver.find_elements(By.XPATH,"(//div[@class='UkUFwK'])")
  new_price=driver.find_elements(By.XPATH,"(//div[@class='Nx9bqj'])")
  for t in title:
    titles.append(t.text)
  for c in color:
    colors.append(c.text)
  for s in star:
    stars.append(s.text)
  for r in review:
    reviews.append(r.text)
  for old in old_price:
    old_prices.append(old.text)
  for d in discount:
    discounts.append(d.text)
  for new in new_price:
    new_prices.append(new.text)
next_button=driver.find_element(By.XPATH,"(//a[@class='_9QVEpD'])")
next_button.click()

time.sleep(5)

min_len=min(len(titles),len(colors),len(stars),len(reviews),len(old_prices),len(discounts),len(new_prices))
titles=titles[:min_len]
colors=colors[:min_len]
stars=stars[:min_len]
reviews=reviews[:min_len]
old_prices=new_prices[:min_len]
discounts=discounts[:min_len]
new_prices=new_prices[:min_len]

df=pd.DataFrame({'Titles':titles,
                 'Colors':colors,
                 'Stars':stars,
                 'Reviews':reviews,
                 'Old Prices':old_prices,
                 'Discounts':discounts,
                 'New Prices':new_prices})

print(df)

df.to_csv(r"C:\Users\Administrator\OneDrive\Documents\Projects\Blankets.csv",index=False)
