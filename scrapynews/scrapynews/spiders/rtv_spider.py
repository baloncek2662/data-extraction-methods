import scrapy

spider_name = 'rtv'

class RtvSpider(scrapy.Spider):
    name = spider_name
    save_files=False

    def start_requests(self):
        save_files_attr = getattr(self, 'save-files', None)
        if save_files_attr == 'True':
            self.save_files = True
            
        # TODO import from ../../../constants.py - URLS_RTVSLO
        urls = [
            'https://www.rtvslo.si/slovenija',
            'https://www.rtvslo.si/svet',
            'https://www.rtvslo.si/sport',
            'https://www.rtvslo.si/kultura',
            'https://www.rtvslo.si/svet-zabave',
        ]
        for url in urls:
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
        article_titles = response.xpath('//a[contains(@aria-label,"")]/text()').getall()
        return self.get_trimmed_list(article_titles)

    def get_trimmed_list(self, l):
        result = []
        for el in l:
            el = el.replace('\n', '')
            el = el.strip()
            if el != '':
                result.append(el)

        return result


