import requests
from bs4 import BeautifulSoup


list_produtos = []

url_base = 'https://www.cec.com.br/busca?q='

produto_nome = input('Qual produto você deseja? ')

response = requests.get(url_base + produto_nome)

site = BeautifulSoup(response.text, 'html.parser')

produtos = site.findAll('div', attrs={'class': 'itemListElement'})

for produto in produtos:

    titulo = produto.find('a', attrs={'class': 'name-and-brand'})

    link = produto.find('a', attrs={'class': 'name-and-brand'})

    preco = produto.find('span', attrs={'class': 'value-full'})



    print('Titulo do Produto:', titulo.text)
    print('Preço do produto: R$', preco.text)
    print('Link do produto:', 'https://www.cec.com.br' + link['href'])
    print('\n\n')

