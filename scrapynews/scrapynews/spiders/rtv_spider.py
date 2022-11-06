import scrapy
from .root_spider import RootSpider


class RtvSpider(scrapy.Spider, RootSpider):
    name = "rtvslo"

    def initialize(self):
        self.save_files = False
        if getattr(self, "save-files", None) == "True":
            self.save_files = True
        self.xpath_expression = '//a[contains(@aria-label,"")]/text()'

    def start_requests(self):
        self.initialize()

        for url in self.get_local_urls_list():
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        if self.save_files:
            article = response.url.split("/")[-2]
            filename = f"./scraped-content/{self.name}-{article}.html"
            with open(filename, "wb") as f:
                f.write(response.body)

        article_data_list = self.get_article_data_list(response)
        yield {self.name: article_data_list}

        # NOT IN USE - use when urls are topics
        # article_titles = self.get_all_titles(response)

    def get_article_data_list(self, response):
        title = response.xpath("//h1/text()").get()
        subtitle = response.xpath('//p[has-class("lead")]/text()').get()
        content = self.get_article_content(response)
        image_captions_list = response.xpath("//figcaption/text()").getall()
        image_captions_list_trimmed = []
        # we need to trim \t and \n from list and remove empty elements
        for item in image_captions_list:
            item_split = item.split()
            item_joined = " ".join(item_split)
            if item_joined:
                image_captions_list_trimmed.append(item_joined)
        return {
            "title": title,
            "subtitle": subtitle,
            "content": content,
            "image_captions_list": image_captions_list_trimmed,
        }

    def get_article_content(self, response):
        content_list = response.xpath(
            '//div[has-class("article-body")]//p/text()'
        ).getall()
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
