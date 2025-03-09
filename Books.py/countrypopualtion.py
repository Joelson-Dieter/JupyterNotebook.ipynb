import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
web="https://www.populationpyramid.net/population-size-per-country/2024/"
path=r"C:\Users\Administrator\OneDrive\Documents\Data_Entry\PythonDOCS\chromedriver.exe"
service=Service(executable_path=path)
driver=webdriver.Chrome(service=service)
driver.get(web)
time.sleep(2)
population_results=[]
countries=driver.find_elements(By.XPATH,"//tbody/tr/td[3]")
populations=driver.find_elements(By.XPATH,"//tbody/tr/td[4]")
for i in range(len(countries)):
  temporary_data={'Country':countries[i].text,'Population':populations[i].text}
  population_results.append(temporary_data)
df_data=pd.DataFrame(population_results)
print(df_data)
df_data.to_csv(r"C:\Users\Administrator\OneDrive\Documents\WebTables\Populations.csv",index=False)