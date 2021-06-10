import scrapy
from .root_spider import RootSpider
from constants import URLS_RTVSLO

spider_name = 'rtvslo'

class RtvSpider(scrapy.Spider, RootSpider):
    name = spider_name

    def initialize(self):
        self.save_files = False
        if getattr(self, 'save-files', None) == 'True':
            self.save_files = True
        self.xpath_expression = '//a[contains(@aria-label,"")]/text()'

    def start_requests(self):
        self.initialize()
            
        for url in URLS_RTVSLO:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        if self.save_files:
            article = response.url.split("/")[-2]
            filename = f'./scraped-content/{spider_name}-{article}.html'
            with open(filename, 'wb') as f:
                f.write(response.body)

        
        article_titles = self.get_all_titles(response)
        yield {'titles' : article_titles}


    def get_all_titles(self, response):
        return super().get_all_titles(response)


