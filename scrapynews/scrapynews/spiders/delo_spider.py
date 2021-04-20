import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)

# article_names = response.xpath('//span[has-class("article_teaser__title_text")]/text()').getall()
# def trim_element(el):
#     el = el.replace('\n', '')
#     el = el.strip()
#     return el
# article_names = map(trim_element , article_names)
# article_names = list(article_names)