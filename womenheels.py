import requests
import pandas as pd
from bs4 import BeautifulSoup

names_list = []
color_size_list = []
prices_list = []
discounts_list = []

for i in range(1,10):

  url = "https://www.flipkart.com/womens-footwear/heels/pr?sid=osp%2Ciko%2C6q1&fm=neo%2Fmerchandising&iid=M_73b5dc13-af52-4b59-bcc8-f8aadc3f1ea0_1_372UD5BXDFYS_MC.416MUHZDV29Y&otracker=hp_rich_navigation_3_1.navigationCard.RICH_NAVIGATION_Fashion%7EWomen%2BFootwear%7EWomen%2BHeels_416MUHZDV29Y&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_3_L2_view-all&cid=416MUHZDV29Y&page"+str(i)

  response = requests.get(url)

  soup = BeautifulSoup(response.text, 'lxml')

  names = soup.find_all('div', class_='syl9yP')
  for name in names:
    names_list.append(name.text.strip())


  color_size = soup.find_all ('div',class_='Br9IW+')
  for color in color_size:
    color_size_list.append(color.text.strip())

  prices = soup.find_all ('div',class_='Nx9bqj')
  for price in prices:
    prices_list.append(price.text.strip())

  discounts = soup.find_all ('div',class_='UkUFwK')
  for discount in discounts:
    discounts_list.append(discount.text.strip())

min_len = min(len(names_list),len(color_size_list),len(prices_list),len(discounts_list))
names_list = names_list [:min_len]
color_size_list = color_size_list [:min_len]
prices_list = prices_list [:min_len]
discounts_list = discounts_list [:min_len]

df=pd.DataFrame({'Names':names_list,'Color & Size':color_size_list,'Discounts':discounts_list,'Price':prices_list})

print(df)

df.to_csv(r'C:\Users\Administrator\OneDrive\Documents\Projects\flipkart_heels.csv', index=False)