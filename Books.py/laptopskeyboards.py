import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

web="https://www.flipkart.com/laptop-accessories/keyboards/pr?sid=6bo,ai3,3oe&fm=neo%2Fmerchandising&iid=M_46721145-2ee0-46c4-81b5-87a2023e3f7a_1_372UD5BXDFYS_MC.4W6EDOSQC5TY&otracker=hp_rich_navigation_3_1.navigationCard.RICH_NAVIGATION_Electronics~Laptop%2BAccessories~Laptop%2BKeyboards_4W6EDOSQC5TY&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_3_L2_view-all&cid=4W6EDOSQC5TY"
path=r"C:\Users\Administrator\OneDrive\Documents\Data_Entry\PythonDOCS\chromedriver.exe"

service=Service(executable_path=path)
driver=webdriver.Chrome(service=service)
driver.get(web)
time.sleep(2)

titles=[]
colors=[]
stars=[]
reviews=[]
discounts=[]
prices=[]

for i in range(501):
  title=driver.find_elements(By.XPATH,"(//a[@class='wjcEIp'])")
  color=driver.find_elements(By.XPATH,"(//div[@class='NqpwHC'])")
  star=driver.find_elements(By.XPATH,"(//div[@class='XQDdHH'])")
  review=driver.find_elements(By.XPATH,"(//span[@class='Wphh3N'])")
  discount=driver.find_elements(By.XPATH,"(//div[@class='UkUFwK'])")
  price=driver.find_elements(By.XPATH,"(//div[@class='Nx9bqj'])")

  for t in title:
    titles.append(t.text)

  for  c in color:
    colors.append(c.text)

  for s in star:
    stars.append(s.text)

for r in review:
  reviews.append(r.text)

  for d in discount:
    discounts.append(d.text)

  for p in price:
    prices.append(p.text)

next_button=driver.find_element(By.XPATH,"(//a[@class='_9QVEpD'])")
next_button.click()
time.sleep(3)

print(titles)
print(colors)
print(stars)
print(reviews)
print(discounts)
print(prices)

min_len=min(len(titles),len(colors),len(stars),len(reviews),len(discounts),len(prices))
titles=titles[:min_len]
colors=colors[:min_len]
stars=stars[:min_len]
reviews=reviews[:min_len]
discounts=discounts[:min_len]
prices=prices[:min_len]

df=pd.DataFrame({'Tiles':titles,
                 'Colors':colors,
                 'Stars':stars,
                 'Reviews':reviews,
                 'Discounts':discounts,
                 'Prices':prices})

print(df)
df.to_csv(r"C:\Users\Administrator\OneDrive\Documents\ApplePhones\LaptopsKeyboards.csv",index=False)