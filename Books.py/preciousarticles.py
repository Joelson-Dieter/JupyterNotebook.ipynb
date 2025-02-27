import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

web="https://www.flipkart.com/jewellery/precious-articles/pr?sid=mcr%2Cpyi&otracker=categorytree&p%5B%5D=facets.price_range.from%3D300&p%5B%5D=facets.price_range.to%3DMax&fm=neo%2Fmerchandising&iid=M_11e9011b-db33-4c25-a612-bdc8b5397220_1_372UD5BXDFYS_MC.EY81DZ32WG7R&otracker=hp_rich_navigation_6_1.navigationCard.RICH_NAVIGATION_Fashion~Watches%2Band%2BAccessories~Precious%2BArticles_EY81DZ32WG7R&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_6_L2_view-all&cid=EY81DZ32WG7R"
path=r"C:\Users\Administrator\OneDrive\Documents\Data_Entry\PythonDOCS\chromedriver.exe"

service=Service(executable_path=path)
driver=webdriver.Chrome(service=service)

driver.get(web)
time.sleep(2)

names=[]
titles=[]
old_prices=[]
discounts=[]
new_prices=[]

for i in range(36):
  name=driver.find_elements(By.XPATH,"(//div[@class='syl9yP'])")
  title=driver.find_elements(By.XPATH,"(//a[@class='WKTcLC BwBZTg'])")
  old_price=driver.find_elements(By.XPATH,"(//div[@class='yRaY8j'])")
  discount=driver.find_elements(By.XPATH,"(//div[@class='UkUFwK'])")
  new_price=driver.find_elements(By.XPATH,"(//div[@class='Nx9bqj'])")

  for n in name:
    names.append(n.text)

  for t in title:
    titles.append(t.text)

  for old in old_price:
    old_prices.append(old.text)

  for d in discount:
    discounts.append(d.text)

  for new in new_price:
    new_prices.append(new.text)

next_button=driver.find_element(By.XPATH,"(//a[@class='_9QVEpD'])")
next_button.click()
time.sleep(2)

min_len=min(len(names),len(titles),len(old_prices),len(discounts),len(new_prices))
names=names[:min_len]
titles=titles[:min_len]
old_prices=old_prices[:min_len]
discounts=discounts[:min_len]
new_prices=new_prices[:min_len]

df=pd.DataFrame({'Names':names,'Titles':titles,'Old prices':old_prices,'Discounts':discounts,'New prices':new_prices})

print(df)


df.to_csv(r"C:\Users\Administrator\OneDrive\Documents\Projects\Precious articles.csv",index=False)

