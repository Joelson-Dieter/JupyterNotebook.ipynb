from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

PATH = r"C:\Users\Administrator\OneDrive\Documents\Data_Entry\PythonDOCS\chromedriver.exe"

service = Service(executable_path = PATH)

driver = webdriver.Chrome(service = service)

driver.get("https://www.ebay.co.uk/?mkcid=1&mkrid=710-53481-19255-0&siteid=3&campid=5338626673&toolid=20008&mkevt=1&customid=engbtopsitescurateana")

sleep(5)

driver.quit()