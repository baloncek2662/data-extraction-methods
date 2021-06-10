import scrapy
from .root_spider import RootSpider
from constants import URLS_DELO

SPIDER_NAME = 'delo'

class DeloSpider(scrapy.Spider, RootSpider):
    name = SPIDER_NAME

    def initialize(self):
        self.save_files = False
        if getattr(self, 'save-files', None) == 'True':
            self.save_files = True
        self.xpath_expression = '//span[has-class("article_teaser__title_text")]/text()'

    # scrapy's built in __init__ does not accept self.save_files, self.xpath_expression
    # LOG: builtins.TypeError: __init__() got an unexpected keyword argument 'save-files'
    def start_requests(self):
        self.initialize()

        for url in URLS_DELO:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        if self.save_files:
            article = response.url.split("/")[-2]
            filename = f'./scraped-content/{SPIDER_NAME}-{article}.html'
            with open(filename, 'wb') as f:
                f.write(response.body)

        
        article_titles = self.get_all_titles(response)
        yield {'titles' : article_titles}

        # NOT IN USE - use when urls are specific articles
        #article_data_list = self.get_article_data_list(response)

    def get_all_titles(self, response):
        return super().get_all_titles(response)





        
    # NOT IN USE - needs to scrape from different urls (www.delo.si)
    def get_article_data_list(self, response):
        title = response.xpath('//h1[has-class("article__title")]/text()').get()
        subtitle = response.xpath('//div[has-class("article__subtitle")]/text()').get()
        content = self.get_article_content(response)
        image_captions_list = response.xpath('//div[has-class("article__image-caption")]/text()').getall()
        return {
            'title': title,
            'subtitle': subtitle,
            'content': content,
            'image_captions_list': image_captions_list,
        }

    def get_article_content(self, response):
        content_list = response.xpath('//div[has-class("article__content")]/text()').getall()
        content = ''
        for el in content_list:
            el = el.replace('\n', '')
            el = el.strip()
            if el != '':
                content += el

        return content
