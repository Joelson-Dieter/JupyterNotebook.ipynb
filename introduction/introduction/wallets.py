import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

web = "https://www.flipkart.com/bags-wallets-belts/wallets-clutches/wallets/pr?sid=reh%2Ccca%2Ch76&marketplace=FLIPKART&p%5B%5D=facets.ideal_for%255B%255D%3DMen&p%5B%5D=facets.ideal_for%255B%255D%3DBoys&p%5B%5D=facets.serviceability%5B%5D%3Dtrue&otracker=nmenu_sub_Men_0_Wallets&fm=neo%2Fmerchandising&iid=M_ddfee4e9-5893-4981-9aa3-82a790ec90bd_1_372UD5BXDFYS_MC.OC9LVYRSIXOM&otracker=hp_rich_navigation_3_1.navigationCard.RICH_NAVIGATION_Fashion~Watches%2Band%2BAccessories~Wallets_OC9LVYRSIXOM&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_3_L2_view-all&cid=OC9LVYRSIXOM"
path = r"C:\Users\Administrator\OneDrive\Documents\Data_Entry\PythonDOCS\chromedriver.exe"

service =  Service (executable_path = path)
driver = webdriver.Chrome (service=service)
driver.get (web)
time.sleep(10)

names = []
old_prices = []
discounts = []
new_prices = []

for i in range (1000):
  name = driver.find_elements (By.XPATH,"(//div[@class='syl9yP'])")
  for n in name:
    names.append(n.text)

  old_price = driver.find_elements (By.XPATH,"(//div[@class='yRaY8j'])")
  for old in old_price:
    old_prices.append(old.text)
    
  discount = driver.find_elements (By.XPATH,"(//div[@class='UkUFwK'])")
  for d in discount:
    discounts.append(d.text)
    
  new_price = driver.find_elements (By.XPATH,"(//div[@class='Nx9bqj'])")
  for new in new_price:
    new_prices.append(new.text)
      
next_button = driver.find_element (By.XPATH,"(//a[@class='_9QVEpD'])")    
next_button.click()

time.sleep(10)

df=pd.DataFrame ({'Names':names,'Old price':old_prices,'Discounts':discounts,'New prices':new_prices})
print(df)

df.to_csv(r"C:\Users\Administrator\OneDrive\Documents\Projects\Wallets.csv",index=False)