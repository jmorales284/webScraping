from selenium import webdriver 
from selenium.webdriver.common.by import By
import pandas as pd

url = "https://www.paginasamarillas.com.co/servicios/farmacias"
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window() 

data = {'name': [], 'address': [], 'webpage': [], 'phone': []}

elements = driver.find_elements(By.CSS_SELECTOR, ".advertise.Advertise_advertise__wUfbF.high.Advertise_high__pUp9O")    
for item in elements:
    data["name"].append(item.find_element(By.CSS_SELECTOR, ".title.Advertise_title__9FF4M>a").text)
    data["address"].append(item.find_element(By.CSS_SELECTOR, ".address.Advertise_address__Nb86U>div>b").text)
    data["webpage"].append(item.find_element(By.CSS_SELECTOR, ".address.Advertise_address__Nb86U>a").text)
    data["phone"].append(item.find_element(By.CSS_SELECTOR, ".phone.Advertise_phone__HDuX5").text)
    
driver.quit()

df = pd.DataFrame(data)
df.to_csv("NombreDelaBasedeDatos.csv", index=False) 
