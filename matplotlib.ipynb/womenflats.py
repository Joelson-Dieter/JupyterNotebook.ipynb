import requests 
from bs4 import BeautifulSoup
import pandas as pd

names_list = []
descs_list = []
comments_list = []
discounts_list = []
prices_list = []

for i in range (1, 100):
  url = "https://www.flipkart.com/womens-footwear/flats/pr?sid=osp%2Ciko%2C9d5&fm=neo%2Fmerchandising&iid=M_41680707-314c-4f99-af5e-83b3fa158fef_1_372UD5BXDFYS_MC.I20M5XEF12IK&otracker=hp_rich_navigation_2_1.navigationCard.RICH_NAVIGATION_Fashion%7EWomen%2BFootwear%7EWomen%2BFlats_I20M5XEF12IK&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_2_L2_view-all&cid=I20M5XEF12IK&page"+str(i)

  response = requests.get (url)
  soup = BeautifulSoup (response.text,'lxml')

  names = soup.find_all ('div',class_='syl9yP')
  for name in names:
    names_list.append(name.text.strip())

  descs = soup.find_all ('a',class_='WKTcLC BwBZTg')
  for desc in descs:
    descs_list.append(desc.text.strip())

  comments = soup.find_all ('div',class_='Br9IW+')
  for comment in comments:
    comments_list.append(comment.text.strip())

  discounts = soup.find_all ('div',class_='UkUFwK')
  for discount in discounts:
    discounts_list.append(discount.text.strip())

  prices = soup.find_all ('div',class_='Nx9bqj')
  for price in prices:
    prices_list.append(price.text.strip())
  print(prices_list)

print(names_list)
print(descs_list)
print(comments_list)
print(discounts_list)
print(prices_list)

min_len = min(len(names_list),len(descs_list),len(comments_list),len(discounts_list),len(prices_list))
names_list = names_list [:min_len]
descs_list = descs_list [:min_len]
comments_list = comments_list [:min_len]
discounts_list = discounts_list [:min_len]
prices_list = prices_list [:min_len]

df = pd.DataFrame({'Names':names_list,
                   'Descriptions':descs_list,
                   'Comments':comments_list,
                   'Discounts':discounts_list,
                   'Prices':prices_list
                   })


df.to_csv(r"C:\Users\Administrator\OneDrive\Documents\Projects\Womenflats.csv",index=False)