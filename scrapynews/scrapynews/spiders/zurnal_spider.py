import scrapy
from .root_spider import RootSpider


class ZurnalSpider(scrapy.Spider, RootSpider):
    name = "zurnal"

    def initialize(self):
        self.save_files = False
        if getattr(self, "save-files", None) == "True":
            self.save_files = True
        self.xpath_expression = '//span[has-class("card__title_highlight")]/text()'

    def start_requests(self):
        self.initialize()

        for url in self.get_local_urls_list():
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        if self.save_files:
            saved_filename = response.url.split("/")[-1]
            filename = f"./scraped-content/{saved_filename}.html"
            with open(filename, "wb") as f:
                f.write(response.body)

        article_data_list = self.get_article_data_list(response)
        yield {self.name: article_data_list}

        # NOT IN USE - use when urls are topics
        # article_titles = self.get_all_titles(response)

    def get_article_data_list(self, response):
        title = response.xpath('//h1[has-class("article__title")]/text()').get()
        subtitle = response.xpath('//div[has-class("article__leadtext")]/text()').get()
        content = self.get_article_content(response)
        return {
            "title": title,
            "subtitle": subtitle,
            "content": content,
        }

    def get_article_content(self, response):
        content_list = response.xpath("//p/text()").getall()
        content = ""
        for el in content_list:
            el = el.replace("\n", "")
            el = el.strip()
            if el != "":
                content += el

        return content

    # NOT IN USE - use when urls are topics
    def get_all_titles(self, response):
        return super().get_all_titles(response)
