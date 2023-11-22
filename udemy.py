import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import math
from unidecode import unidecode
from pathlib import Path
import os
import shutil
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


CAMINHO_RAIZ = Path(__file__).parent
caminho = CAMINHO_RAIZ / 'arquivos' / 'lista_cursos.csv'

# Verifica se o arquivo existe
if os.path.exists(caminho):
    os.remove(caminho)
    print(f'O arquivo {caminho} foi excluído com sucesso.')
else:
    print(f'O arquivo {caminho} não existe.')

    # .decode('utf-8')

# eaders = {
 #   'user-Agent':
 #   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
# }


# Configure as opções do Chrome com o User-Agent
options = webdriver.ChromeOptions()
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")


# Instancie o WebDriver
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico, options=options)

url = 'https://www.udemy.com/join/login-popup/'
# url = 'https://www.udemy.com/home/my-courses/learning/'
# url = 'https://www.udemy.com/'
navegador.get(url)
sleep(1)
# login = navegador.find_element(By.CSS_SELECTOR,
#                              '#br > div.ud-main-content-wrapper > div.ud-app-loader.ud-component--header-v6--header.ud-header.ud-app-loaded > div.ud-header.ud-text-sm.desktop-header-module--header--3nb6v.desktop-header-module--flex-middle--1e7c8 > div:nth-child(8) > a'
#                             ).click()

# email = navegador.find_element('xpath', '//*[@id="form-group--1"]')
# email.send_keys('fabiojoaoanastacio@hotmail.com')
# sleep(3)
# senha = navegador.find_element('xpath', '//*[@id="form-group--3"]')
# senha.send_keys('D3lt469')
# sleep(1)


# <input aria-invalid="false" minlength="6" maxlength="64" name="password" required="" id="form-group--1" type="password" class="ud-text-input ud-text-input-large ud-text-md ud-compact-form-control password-form-group--password-input--1WX1K" value="">
username = navegador.find_element(By.ID, "form-group--1")
password = navegador.find_element(By.ID, "form-group--3")

username.send_keys("fabiojoaoanastacio@hotmail.com")
sleep(1)
password.send_keys("D3lt469")
sleep(1)
password.send_keys(Keys.RETURN)
try:
    element = WebDriverWait(navegador, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "ud-sr-only"))
    )
finally:
    pass  # Continue com o restante do código

# password.send_keys(Keys.RETURN)
# print(navegador.current_url)
sleep(15)
# botao = navegador.find_element(  # 'xpath',
# '//button[@type="submit"]'
# By.CLASS_NAME, 'ud-btn ud-btn-large ud-btn-brand ud-heading-md helpers--auth-submit-button--2K2dh'
# )
#   'xpath', '//*[@id="br"]/div[1]/div[2]/div/div/form/button'
# )
# )
# By.XPATH, '<button type="submit" class="ud-btn ud-btn-large ud-btn-brand ud-heading-md helpers--auth-submit-button--2K2dh"><span>Fazer login</span></button>').click()
# 'xpath', '//button[@type="submit"]')
# botao = navegador.find_element_by_xpath('//button[@type="submit"]')
# botao.click()
# sleep(5)
# html_elemento = botao.get_attribute('outerHTML')

# soup = BeautifulSoup(html_elemento, 'html.parser')

# print(soup.prettify())

# pagina = soup.find_all('button', attrs={
#   'class': "ud-btn ud-btn-large ud-btn-brand ud-heading-md helpers--auth-submit-button--2K2dh"})

# meus_aprendizados = navegador.find_element('xpath',
#                                          '//*[@id="br"]/div[1]/div[2]/div/div[2]/div[1]/div/div[1]/div/a/span'
#                                         )
# sleep(1)
# meus_aprendizados.click()
# botao.send_keys(Keys.ENTER)
# sleep(5)

# navegador.execute_script(
#   "window.location.href = 'https://www.udemy.com/home/my-courses/learning/'")

# url = 'https://www.udemy.com/home/my-courses/learning/'
# url = 'https://www.udemy.com/'
# navegador.get(url)
# print(navegador.current_url)

# class="ud-btn ud-btn-large ud-btn-brand ud-heading-md helpers--auth-submit-button--2K2dh

# br > div.ud-main-content-wrapper > div.ud-main-content > div > div > form > button

# //*[@id="br"]/div[1]/div[2]/div/div/form/button


# print(soup.prettify())

# login = soup.find('a', attrs={
#                 'href': "https://www.udemy.com/join/login-popup/?locale=pt_BR&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2Fmobile%2Fipad%2F"})

# print(login)
navegador.quit()
