import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

web = "https://www.flipkart.com/watches/wrist-watches/pr?sid=r18,f13&p[]=facets.ideal_for%255B%255D%3DCouple&p[]=facets.ideal_for%255B%255D%3DWomen&p[]=facets.ideal_for%255B%255D%3DMen%2B%2526%2BWomen&p[]=facets.ideal_for%255B%255D%3DMen&otracker=categorytree&fm=neo%2Fmerchandising&iid=M_07f52270-c013-4914-add0-480382314207_1_372UD5BXDFYS_MC.CI9JK83AKS5H&otracker=hp_rich_navigation_6_1.navigationCard.RICH_NAVIGATION_Fashion~Watches%2Band%2BAccessories_CI9JK83AKS5H&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_6_L1_view-all&cid=CI9JK83AKS5H"

path = r"C:\Users\Administrator\OneDrive\Documents\Data_Entry\PythonDOCS\chromedriver.exe"

service = Service (executable_path=path)
driver = webdriver.Chrome (service=service)

driver.get(web)
time.sleep(1)

names = []
old_prices = []
discounts = []
new_prices = []

for i in range (1,5):
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
  
  next_button = driver.find_elements (By.XPATH,"(//a[@class='_9QVEpD'])")
  next_button[0].click()
  time.sleep(2)

  print(len(names))
  print(len(old_prices))
  print(len(discounts))
  print(len(new_prices))
