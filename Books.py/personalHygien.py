import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

web = "https://www.flipkart.com/beauty-and-grooming/~cs-e7292xfj9c/pr?sid=g9b&collection-tab-name=Personal+Hygiene&p%5B%5D=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&fm=neo%2Fmerchandising&iid=M_f363f7ba-cff6-4549-9b77-93937aad994a_1_372UD5BXDFYS_MC.U3O9OH173G67&otracker=hp_rich_navigation_3_1.navigationCard.RICH_NAVIGATION_Beauty%2C%2BToys%2B%26%2BMore~Beauty%2B%26%2BPersonal%2BCare~Personal%2BHygiene_U3O9OH173G67&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_3_L2_view-all&cid=U3O9OH173G67"
path = r"C:\Users\Administrator\OneDrive\Documents\Data_Entry\PythonDOCS\chromedriver.exe"

service = Service (executable_path=path)
driver = webdriver.Chrome (service=service)

driver.get (web)
time.sleep(2)

titles=[]
stars=[]
reviews=[]
discounts=[]
prices=[]

for i in range (1,1118):
  title = driver.find_elements(By.XPATH,"(//a[@class='wjcEIp'])")
  star = driver.find_elements(By.XPATH,"(//div[@class='XQDdHH'])")
  review = driver.find_elements(By.XPATH,"(//span[@class='Wphh3N'])")
  discount = driver.find_elements(By.XPATH,"(//div[@class='UkUFwK'])")
  price = driver.find_elements(By.XPATH,"(//div[@class='Nx9bqj'])")

  for t in title:
    titles.append(t.text)

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
time.sleep(2)

min_len = min(len(titles),len(stars),len(reviews),len(discounts),len(prices))
titles=titles [:min_len]
stars=stars [:min_len]
reviews=reviews [:min_len]
discounts=discounts [:min_len]
prices=prices [:min_len]

df=pd.DataFrame({'Titles':titles,
                 'Stars':stars,
                 'Reviews':reviews,
                 'Discounts':discounts,
                 'Prices':prices})

print(df)

df.to_csv(r"C:\Users\Administrator\OneDrive\Documents\Projects\Personal Hygiene.csv",index=False)