# Динамические сайты
# Некоторые сайты формируют страницы, показываемые пользователю, динамически, на стороне сервера
# Что осложняет процесс парсинга подобных страниц
# Один из популярных приемов на таких сайтах используют "бесконечную прокрутку"
# В итоге, при достижении "конца" страницы, страница изменяется и добовляется новый контент.
# Пробуем решить эту задачу, использую еще одну стороннюю библиотеку - Scrapy
# scrapy.org
# Ее интересной особенностью является то,
# что для каждой определенной задачи мы создаем своего "паука"
# Указываем ему диапазон страниц, которые он должен посетить
# Наделяем методами, организующими сбор информации,
# И запускаем

# Первым делом (после установки) нам понадобится создать отдельный  проект для него:
# scrapy startproject <name>
# далее написать самого "паука", создав файл в директории spiders
# Код нащего паучка:
# https://digitology.tech/docs/scrapy/intro/tutorial.html
import json
import scrapy


class SpidyQuotesSpider(scrapy.Spider):
    name = 'spidyquotes'
    quotes_base_url = 'http://spidyquotes.herokuapp.com/api/quotes?page=%s'
    start_urls = [quotes_base_url % 1]
    download_delay = 1.5

    def parse(self, response):
        data = json.loads(response.body)
        for item in data.get('quotes', []):
            yield {
                'text': item.get('text'),
                'author': item.get('author', {}).get('name'),
                'tags': item.get('tags'),
            }
        if data['has_next']:
            next_page = data['page'] + 1
            yield scrapy.Request(self.quotes_base_url % next_page)