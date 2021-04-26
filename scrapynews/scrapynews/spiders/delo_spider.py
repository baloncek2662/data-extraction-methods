import scrapy

spider_name = 'delo'

class DeloSpider(scrapy.Spider):
    name = spider_name
    save_files=False

    def start_requests(self):
        save_files_attr = getattr(self, 'save-files', None)
        if save_files_attr == 'True':
            self.save_files = True
            
        # TODO import from ../../../constants.py - URLS_DELO
        urls = [
            'https://www.delo.si/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        if self.save_files:
            page = response.url.split("/")[-2]
            filename = f'./scraped-content/{spider_name}-{page}.html'
            with open(filename, 'wb') as f:
                f.write(response.body)

        
        article_names = response.xpath('//span[has-class("article_teaser__title_text")]/text()').getall()
        def trim_element(el):
            el = el.replace('\n', '')
            el = el.strip()
            return el
        article_names = map(trim_element , article_names)
        article_names = list(article_names)
        print(article_names)
