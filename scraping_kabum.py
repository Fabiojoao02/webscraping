from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
from pathlib import Path
import time
import math
import re
import os


CAMINHO_RAIZ = Path(__file__).parent
caminho = CAMINHO_RAIZ / 'arquivos' / 'preco_cadeira.csv'

# Verifica se o arquivo existe
if os.path.exists(caminho):
    os.remove(caminho)
    print(f'O arquivo {caminho} foi excluído com sucesso.')
else:
    print(f'O arquivo {caminho} não existe.')

# Configuração inicial
url = 'https://www.kabum.com.br/espaco-gamer/cadeiras-gamer'
headers = {
    'user-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()), options=options)

driver.get(url)

time.sleep(2)

soup = BeautifulSoup(driver.page_source, 'html.parser')


qtd_itens = soup.find('div', id='listingCount').get_text().strip()
index = qtd_itens.find(' ')
qtd = qtd_itens[:index]
ultima_pagina = math.ceil(int(qtd) / 20)

# Estrutura de dados para armazenar os resultados
dic_produtos = {'marca': [], 'preco': []}


for i in range(1, ultima_pagina + 1):
    url_pag = f'{url}?page_number={i}&page_size=20&facet_filters=&sort=most_searched'
    driver.get(url_pag)
    time.sleep(2)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    produtos = soup.find_all('div', class_=re.compile('productCard'))

    for produto in produtos:
        marca = produto.find('span', class_=re.compile(
            'nameCard')).get_text().strip()
        preco = produto.find('span', class_=re.compile(
            'priceCard')).get_text().strip()

        print(marca, preco)

        dic_produtos['marca'].append(marca)
        dic_produtos['preco'].append(preco)

    print(url_pag)

driver.quit()

print(caminho)
df = pd.DataFrame(dic_produtos)
df.to_csv(caminho, encoding='utf-8', sep=';')
# print(qtd_itens)
# print(index)
# print(qtd)


# df = pd.DataFrame(dic_produtos)
# df.to_csv('preco_cadeira.csv', encoding='utf-8', sep=';')
