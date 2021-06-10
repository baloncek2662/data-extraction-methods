import scrapy
from .root_spider import RootSpider
from constants import URLS_ZURNAL


SPIDER_NAME = 'zurnal'

class ZurnalSpider(scrapy.Spider, RootSpider):
    name = SPIDER_NAME
    
    def initialize(self):
        self.save_files = False
        if getattr(self, 'save-files', None) == 'True':
            self.save_files = True
        self.xpath_expression = '//span[has-class("card__title_highlight")]/text()'

    def start_requests(self):
        self.initialize()
         
        for url in URLS_ZURNAL:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        if self.save_files:
            article = response.url.split("/")[-2]
            filename = f'./scraped-content/{SPIDER_NAME}-{article}.html'
            with open(filename, 'wb') as f:
                f.write(response.body)

        
        article_titles = self.get_all_titles(response)
        yield {SPIDER_NAME : article_titles}


    def get_all_titles(self, response):
        return super().get_all_titles(response)