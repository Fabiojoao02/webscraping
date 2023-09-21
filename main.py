import requests
from bs4 import BeautifulSoup

link = 'https://www.google.com/search?q=cota%C3%A7%C3%A3o+dolar'

headers = {
    'user-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.36'
}

requisicao = requests.get(link, headers=headers)
print(requisicao)
# print(requisicao.text)
site = BeautifulSoup(requisicao.text, 'html.parser')
# print(site.prettify())

titulo = site.find('title')
# print(titulo)

pesquisa = site.find_all('input')
# print(pesquisa[2])

pesquisa2 = site.find('input', class_='noHIxc')
# print(pesquisa2)
# print(pesquisa2['value'])

cotacao = site.find('span', class_='DFlfde SwHCTb')
print(cotacao['data-value'])
print(cotacao.get_text())
