import scrapy
from .root_spider import RootSpider
from constants import URLS_SLOVENSKE_NOVICE

SPIDER_NAME = 'slovenskenovice'

class SloNoviceSpider(scrapy.Spider, RootSpider):
    name = SPIDER_NAME

    def initialize(self):
        self.save_files = False
        if getattr(self, 'save-files', None) == 'True':
            self.save_files = True
        self.xpath_expression = '//span[has-class("article_teaser__title_text")]/text()'

    def start_requests(self):
        self.initialize()
            
        for url in URLS_SLOVENSKE_NOVICE:
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
