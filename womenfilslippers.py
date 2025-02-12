import pandas as pd
import requests
from bs4 import BeautifulSoup

names_list = []

descriptions_list = []

old_price_list = []

new_price_list = []

discounts_list = []

for i in range (1, 40):

  url ="https://www.flipkart.com/womens-footwear/slippers-flip-flops/pr?sid=osp%2Ciko%2Ciz7&fm=neo%2Fmerchandising&iid=M_780ed50d-eea6-4156-9924-42fe87cede93_1_372UD5BXDFYS_MC.6DZZP5R3P74E&otracker=hp_rich_navigation_5_1.navigationCard.RICH_NAVIGATION_Fashion%7EWomen%2BFootwear%7EWomen%2BSlipper%2BFlip%2BFlops_6DZZP5R3P74E&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_5_L2_view-all&cid=6DZZP5R3P74E&page"+str(i)

  response = requests.get(url)

  soup = BeautifulSoup(response.text, 'lxml')

  names = soup.find_all ('div',class_='syl9yP')
  for name in names:
    names_list.append(name.text.strip())

  descriptions = soup.find_all ('a',class_='WKTcLC')
  for description in descriptions:
    descriptions_list.append(description.text.strip())


  old_price = soup.find_all ('div',class_='yRaY8j')
  for price in old_price:
    old_price_list.append(price.text.strip())

  new_price = soup.find_all ('div',class_='Nx9bqj')
  for price in new_price:
    new_price_list.append(price.text.strip())

  discounts = soup.find_all ('div',class_='UkUFwK')
  for discount in discounts:
    discounts_list.append(discount.text.strip())

print(len(names_list))
print(len(descriptions_list))
print(len(old_price_list))
print(len(new_price_list))
print(len(discounts_list))

min_len = min(len(names_list), len(descriptions_list), len(old_price_list), len(new_price_list),len(discounts_list))

names_list = names_list[:min_len]

descriptions_list = descriptions_list[:min_len]

old_price_list = old_price_list[:min_len]

new_price_list = new_price_list[:min_len]

discounts_list = discounts_list[:min_len]

df = pd.DataFrame({'Names':names_list, 'Descriptions': descriptions_list, 'Old Price': old_price_list, 'New Price': new_price_list, 'Discounts': discounts_list})

print(df)

df

df.to_csv(r"C:\Users\Administrator\OneDrive\Documents\Projects\Women slipper.csv",index= False)