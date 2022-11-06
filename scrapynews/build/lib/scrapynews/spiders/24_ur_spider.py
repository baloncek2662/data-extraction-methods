import scrapy
from .root_spider import RootSpider

SPIDER_NAME = '24ur'


class Spider24ur(scrapy.Spider, RootSpider):
    name = SPIDER_NAME

    def initialize(self):
        self.save_files = False
        if getattr(self, 'save-files', None) == 'True':
            self.save_files = True
        self.xpath_expression = '//span[has-class("card__title-inside")]/text()'

    def start_requests(self):
        self.initialize()

        # TODO import from ../../../constants.py - URLS_24_UR
        urls = [
            'https://www.24ur.com/',
            'https://www.24ur.com/novice/',
            'https://www.24ur.com/sport/',
            'https://www.24ur.com/popin/',
            'https://www.24ur.com/tv-oddaje/',
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
