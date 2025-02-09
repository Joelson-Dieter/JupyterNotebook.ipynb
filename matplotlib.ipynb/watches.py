import requests

from bs4 import BeautifulSoup

import pandas as pd\

titles_list = []

prices_list = []

comments_list = []

origins_list = []

for page in range (1,100):
  url = "https://www.ebay.co.uk/sch/3937/i.html?_nkw=watches&_from=R40&_pgn&{page}"

  response = requests.get (url)

  soup = BeautifulSoup (response.text,'lxml')

  titles=soup.find_all ('div',class_='s-item__title')
  for title in titles:
    titles_list.append(title.text.strip())


  prices = soup.find_all ('span',class_='s-item__price')
  for price in prices:
    prices_list.append(price.text.strip())

  origins = soup.find_all ('span',class_='s-item__location s-item__itemLocation')
  for origin in origins:
    origins_list.append(origin.text.strip().strip())

print(len(titles_list))
print(len(prices_list))
print(len(origins_list))

min_len = min(len(titles_list),len(prices_list),len(origins_list))

titles_list = titles_list[:min_len]

prices_list = prices_list[:min_len]

origins_list = origins_list[:min_len]

df = pd.DataFrame({'Title': titles_list, 'Price': prices_list, 'Origin': origins_list})

print(df)

df

df.to_csv(r"C:\Users\Administrator\OneDrive\Documents\Projects\watches.csv",index=False)