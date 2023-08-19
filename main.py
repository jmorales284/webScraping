from selenium import webdriver 
from selenium.webdriver.common.by import By
import pandas as pd

url = "https://www.yelp.com/search?find_desc=Delivery&find_loc=San+Francisco%2C+CA&attrs=RestaurantsDelivery&start=0"
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window() 

data = {'name': [], 'description': [], 'address': [], 'typeOfFood' : [], 'information' : []}

elements = driver.find_elements(By.CSS_SELECTOR, ".padding-t3__09f24__TMrIW.padding-r3__09f24__eaF7p.padding-b3__09f24__S8R2d.padding-l3__09f24__IOjKY.border-color--default__09f24__NPAKY")    
for item in elements:

    data["name"].append(item.find_element(By.CSS_SELECTOR, ".css-19v1rkv").text)

    data["description"].append(item.find_element(By.CSS_SELECTOR, ".arrange-unit__09f24__rqHTg.arrange-unit-fill__09f24__CUubG.border-color--default__09f24__NPAKY>.").text)

    data["address"].append(item.find_element(By.CSS_SELECTOR, ".css-dzq7l1 span:nth-child(2)").text)

    data["typeOfFood"].append(item.find_element(By.CSS_SELECTOR, ".css-1iacd0p>.css-11bijt4").text)

    data["information"].append(item.find_element(By.CSS_SELECTOR, ".label__09f24__hNq6C.display--inline__09f24__c6N_k.border-color--default__09f24__NPAKY>p>.raw__09f24__T4Ezm").text)
    
driver.quit()

df = pd.DataFrame(data)
df.to_csv("DatosEstadistica.csv", index=False) 
