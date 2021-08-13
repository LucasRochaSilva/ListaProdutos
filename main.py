from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from time import sleep
import smtplib
import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_podutos = []

response = requests.get = url =('https://www.mercadolivre.com.br/ofertas#nav-header')

content = response.content

site = BeautifulSoup(content, 'html.parser')

driver = webdriver.Chrome()
driver.get(url)


for i in range(1, 20):
    produto = driver.find_element_by_xpath(f'//*[@id="root-app"]/div/section[2]/div/div[2]/div/ol/li[{i}]/a/div/div/p')
    valor = driver.find_element_by_xpath(f'//*[@id="root-app"]/div/section[2]/div/div[2]/div/ol/li[{i}]/a/div/div/div[2]/span/span')
    #produto1 = driver.find_element_by_xpath(f'//*[@id="root-app"]/div/section[2]/div/div[2]/div/ol/li[{i}]/a/div/div/p')

    produto_text = produto.text
    valor_text = valor.text
    #produto1_text = produto1.text

    print(f'Produto : {produto_text}')
    print(f'Valor: {valor_text}')
    #print(f'Produto 1 :{produto1_text}')

