# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests

url = 'https://coinmarketcap.com/ru/'
page = requests.get(url)
print(page.status_code)
if page.status_code == 200:
    filteredNews = []
    allInfo = []
    table = []

    soup = BeautifulSoup(page.text, "html.parser")
    # print(soup)

    # table = soup.findAll('tbody')
    # for i in table:
    #     print(i)
    allInfo = soup.findAll('div', class_='sc-aef7b723-0 sc-655e743f-0 fmYNap')
    print(len(allInfo))
    for i in allInfo:
        print(i.get_text())

    for data in allInfo:
        data.find('p', class_='sc-4984dd93-0 kKpPOn')
        filteredNews.append(data.text)
    print(len(filteredNews))

    for data in filteredNews:
        print(data)


