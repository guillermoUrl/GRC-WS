# Importar paquetes de Sistema Operativo
import time
import os
# Importar paquete para WebScrape
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Se consiguen los directorios de Trabajo
CurrentDir = os.getcwd()
CroniumPath = CurrentDir + "\GTC\Cronium\chromedriver.exe"

# Se establecen las Variables
driver = webdriver.Chrome(CroniumPath)
inputdata = "Molecula"
BaseLink = "https://www.guatecompras.gt/concursos/consultaConAvanz.aspx"

# Inicia Scrip
# Se ingresa al Link
driver.get(BaseLink)
# Busca Searchbox, ingresa varibale a buscar
search = driver.find_element_by_id("MasterGC_ContentBlockHolder_txtTexto")
search.send_keys(inputdata)
sendrequest = driver.find_element_by_id(
    "MasterGC_ContentBlockHolder_btnBuscar")
sendrequest.click()

time.sleep(5)
# Cierra Scrip
driver.close()
