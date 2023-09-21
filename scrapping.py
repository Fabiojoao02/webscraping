import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import math
from unidecode import unidecode
from pathlib import Path
import os
import shutil


CAMINHO_RAIZ = Path(__file__).parent
caminho = CAMINHO_RAIZ / 'arquivos' / 'preco_cadeira.csv'

# Verifica se o arquivo existe
if os.path.exists(caminho):
    os.remove(caminho)
    print(f'O arquivo {caminho} foi excluído com sucesso.')
else:
    print(f'O arquivo {caminho} não existe.')

url = 'https://www.kabum.com.br/espaco-gamer/cadeiras-gamer'

headers = {
    'user-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}

site = requests.get(url, headers=headers)
# site.encoding = 'ISO-8859-1'
soup = BeautifulSoup(site.content, 'html.parser')
qtd_itens = soup.find('div', id='listingCount').get_text().strip()

index = qtd_itens.find(' ')
qtd = qtd_itens[:index]

ultima_pagina = math.ceil(int(qtd)/20)
dic_produtos = {
    'marca': [],
    'preco': [],
    'preco_old': [],
    'preco_cond_avista': []
}

for i in range(1, ultima_pagina+1):
    url_pag = f'https://www.kabum.com.br/espaco-gamer/cadeiras-gamer?page_number={i}&page_size=20&facet_filters=&sort=most_searched'
    site = requests.get(url_pag, headers=headers)
    # site.encoding = 'ISO-8859-1'
    soup = BeautifulSoup(site.content, 'html.parser')
    produtos = soup.find_all('div', class_=re.compile('productCard'))
    for produto in produtos:
        marca = unidecode(produto.find('span', class_=re.compile(
            'nameCard')).get_text().strip())
        preco = produto.find('span', class_=re.compile(
            'priceCard')).get_text().strip()
        preco_old = produto.find('span', class_=re.compile(
            'oldPriceCard')).get_text().strip()
        preco_avista = produto.find('span', class_=re.compile(
            'priceTextCard')).get_text().strip()
        # print(marca, preco)

        dic_produtos['marca'].append(marca)
        dic_produtos['preco'].append(preco)
        dic_produtos['preco_old'].append(preco_old)
        dic_produtos['preco_cond_avista'].append(preco_avista)
        # print(preco)

    # print(url_pag)

print(caminho)
df = pd.DataFrame(dic_produtos)
df.to_csv(caminho, encoding='utf-8', sep=';')
# print(qtd_itens)
# print(index)
# print(qtd)
