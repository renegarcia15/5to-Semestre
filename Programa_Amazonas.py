#Selenium


import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

s= Service(ChromeDriverManager().install())
opc=Options()
opc.add_argument("--windows-size=1020,1200")



navegador=webdriver.Chrome(service=s,options=opc)
navegador.get("https://www.amazon.com.mx/")
txt=navegador.find_element(By.ID,"twotabsearchtextbox")
producto=input("Que producto vas a buscar---> ")
txt.send_keys(producto)
time.sleep(2)
"""password=navegador.find_element(By.NAME,"pass")
password.send_keys("Tainy")
time.sleep(2)"""

sesion=navegador.find_element(By.ID,"nav-search-submit-button")
sesion.click()
navegador.find_elements()
navegador.save_screenshot("Producto.png")
print(navegador.title)
time.sleep(3)