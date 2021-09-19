import os
import glob
from constants import SCRAPE_DEST_FOLDER

class RootSpider():
    def __init__(self):
        self.xpath_expression = ''

    def get_all_titles(self, response):
        article_titles = response.xpath(self.xpath_expression).getall()
        return self.get_trimmed_list(article_titles)

    def get_trimmed_list(self, l):
        result = []
        for el in l:
            el = el.replace('\n', '')
            el = el.strip()
            if el != '':
                result.append(el)

        return result

    def get_local_urls_list(self):
        urls_dir = f'{SCRAPE_DEST_FOLDER}{self.name}/{self.name}/*'
        paths = glob.glob(urls_dir)
        # add file:// prefix to make valid url out of path
        return [f'file://{p}' for p in paths] 

