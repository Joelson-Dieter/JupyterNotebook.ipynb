import requests
import pandas as pd
from bs4 import BeautifulSoup

names_list = []
locations_list = []
addresses_list = []
descs_list = []
value_list = []

for i in range (1, 22):
  url = "https://www.property24.co.ke/property-for-sale-in-nanyuki-c1868?Page=1"
  response = requests.get(url)
  soup = BeautifulSoup(response.text,'lxml')
  names = soup.find_all ('span',class_='p24_propertyTitle')
  for name in names:
    names_list.append(name.text.strip())

  locations = soup.find_all ('span',class_='p24_location')
  for location in locations:
    locations_list.append(location.text.strip())

  addresses = soup.find_all('span',class_='p24_address')
  for address in addresses:
    addresses_list.append(address.text.strip())

  descs = soup.find_all ('span',class_='p24_excerpt')
  for desc in descs:
    descs_list.append(desc.text.strip())

  value = soup.find_all ('span',class_='p24_price')
  for price in value:
    value_list.append(price.text.strip())

print(len(names_list))
print(len(locations_list))
print(len(addresses_list))
print(len(descs_list))
print(len(value_list))  

df = pd.DataFrame({
    'Name': names_list,
    'Location': locations_list,
    'Address': addresses_list,
    'Description': descs_list,
    'Value': value_list})
    
print(df)

df.to_csv(r"C:\Users\Administrator\OneDrive\Documents\Projects\Plots & Houses for sale in Nanyuki.csv", index=False)