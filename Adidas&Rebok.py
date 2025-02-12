import requests
import pandas as pd
from bs4 import BeautifulSoup

names_list = []

discounts_list = []

prices_list = []

for i in range (1, 100):

  url = "https://www.flipkart.com/footwear/pr?sid=osp&otracker=categorytree&page"+str(i)
  response = requests.get(url)
  soup = BeautifulSoup(response.text,'lxml')

  names = soup.find_all ('div',class_='syl9yP')
  for name in names:
    names_list.append(name.text.strip())

  discounts = soup.find_all ('div',class_='UkUFwK')
  for discount in discounts:
    discounts_list.append(discount.text.strip())

  prices = soup.find_all ('div',class_='Nx9bqj')
  for price in prices:
    prices_list.append(price.text.strip())


min_len = min(len(names_list), len(discounts_list),len(prices_list))

names_list = names_list[:min_len]

discounts_list = discounts_list[:min_len]

prices_list = prices_list[:min_len]

df = pd.DataFrame({'Names':names_list, 'Discounts':discounts_list, 'Prices':prices_list})

print(df)

df.to_csv(r"C:\Users\Administrator\OneDrive\Documents\Adidas&Reboc.csv",index=False)