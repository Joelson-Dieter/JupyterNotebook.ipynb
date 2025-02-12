from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service = Service (r"C:\Users\Administrator\OneDrive\Documents\Data_Entry\PythonDOCS\chromedriver.exe")

driver = webdriver.Chrome (service=service)

driver.get("https://www.flipkart.com/")

input_search = driver.find_elements (By.XPATH,"(//input[@class='Pke_EE'])")
search_button = driver.find_elements (By.XPATH,"(//button[@class='_2iLD__'])")
input_search[0].send_keys ("Tshirts")
sleep(1)

search_button[0].click()

products = []

for i in range (30):
  product = driver.find_elements (By.XPATH,"(//div[@class='syl9yP'])")
  for p in product:
    products.append(p.text.strip())
next_button = driver.find_elements(By.XPATH,"(//a[@class='_9QVEpD'])")
next_button[0].click()

sleep(5)

print(product)
  