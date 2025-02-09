import requests
from bs4 import BeautifulSoup
import pandas as pd

titles_list = []

previousPrice_list = []

currentPrice_list = []

comments_list = []


url = "https://www.ebay.com/b/Womens-Bags-Handbags/169291/bn_738272"

response = requests.get (url)

soup = BeautifulSoup (response.text,'lxml')

titles = soup.find_all ('h3',class_='textual-display bsig__title__text')
for title in titles:
  titles_list.append(title.text.strip())


previousPrice = soup.find_all ('span',class_='textual-display bsig__generic bsig__previousPrice strikethrough')
for price in previousPrice:
  previousPrice_list.append(price.text.strip())

currentPrice = soup.find_all('div',class_='bsig brw-signal bsig--primary')
for price in currentPrice:
  currentPrice_list.append(price.text.strip())
print(currentPrice_list)

comments = soup.find_all ('span',class_='textual-display bsig__generic bsig__logisticsCost')
for comment in comments:
  comments_list.append(comment.text.strip())

print(len(titles_list))

print(len(previousPrice_list))

print(len(currentPrice_list))

print(len(comments_list))

min_length = min(len(titles_list), len(previousPrice_list), len(currentPrice_list), len(comments_list))

titles_list = titles_list [:min_length]

previousPrice_list = previousPrice_list [:min_length]

currentPrice_list = currentPrice_list [:min_length]

comments_list = comments_list [:min_length]


df = pd.DataFrame({
  'Title': titles_list,
  'Previous Price': previousPrice_list,
  'Current Price': currentPrice_list})


print(df)

df

df.to_csv(r"C:\Users\Administrator\OneDrive\Documents\Projects\ebay_womens_bags_handbags.csv", index=False)


