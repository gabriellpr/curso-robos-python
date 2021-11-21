from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

print("Iniciando nosso robô...")

driver = webdriver.Chrome(r"C:\\Users\\casa\\Desktop\\Gabriel\\ProjectsPython\\Robos\\chromedriver")
driver.get("https://registro.br")

#Acha a barra de pesquisa
pesquisa = driver.find_element_by_id("is-avail-field")
pesquisa.clear()
pesquisa.send_keys("roboscompython.com.br")
pesquisa.send_keys(Keys.RETURN)

time.sleep(8)
driver.close()