import pandas as pd
from bs4 import BeautifulSoup
import requests

url = "https://www.flipkart.com/air-conditioners/pr?sid=j9e%2Cabm%2Cc54&p%5B%5D=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&p%5B%5D=facets.brand%255B%255D%3DHitachi&p%5B%5D=facets.serviceability%5B%5D%3Dtrue&otracker=categorytree&otracker=nmenu_sub_TVs+%26+Appliances_0_Hitachi&page=1"

response = requests.get (url)

soup = BeautifulSoup (response.text,'lxml')

names = soup.find_all ('div',class_='KzDlHZ')
for name in names:
  print(name.text)

