from bs4 import BeautifulSoup
import requests

# Попробуем с ее помощью получить актуальную
# информацию о курсе доллара, евро и нефти с сайта yandex.ru
response = requests.get('https://yandex.ru/')
if response.status_code == 200:
    html_doc = BeautifulSoup(response.text, features='html.parser')
    print(html_doc)
    list_of_values = html_doc.find_all('span', {'class': 'inline-stocks__value_inner'})
    print(list_of_values)
    list_of_names = html_doc.find_all('a', {'class': 'home-link home-link_black_yes inline-stocks__link'})
    print(list_of_names)

    for names, values in zip(list_of_names, list_of_values):
        print(names.text, values.text)


