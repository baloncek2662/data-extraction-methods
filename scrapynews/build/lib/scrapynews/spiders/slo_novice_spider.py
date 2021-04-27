import scrapy
from .root_spider import RootSpider

SPIDER_NAME = 'slovenske-novice'

class SloNoviceSpider(scrapy.Spider, RootSpider):
    name = SPIDER_NAME

    def initialize(self):
        self.save_files = False
        if getattr(self, 'save-files', None) == 'True':
            self.save_files = True
        self.xpath_expression = '//span[has-class("article_teaser__title_text")]/text()'

    def start_requests(self):
        self.initialize()
            
        # TODO import from ../../../constants.py - URLS_SLOVENSKE_NOVICE
        urls = [
            'https://www.slovenskenovice.si/',
            'https://www.slovenskenovice.si/sport/',
            'https://www.slovenskenovice.si/bralci/',
            'https://www.slovenskenovice.si/kronika/',
            'https://www.slovenskenovice.si/stil/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        if self.save_files:
            article = response.url.split("/")[-2]
            filename = f'./scraped-content/{SPIDER_NAME}-{article}.html'
            with open(filename, 'wb') as f:
                f.write(response.body)

        
        article_titles = self.get_all_titles(response)
        yield {'titles' : article_titles}


    def get_all_titles(self, response):
        return super().get_all_titles(response)
