class RootSpider():
    def __init__(self):
        self.xpath_expression = ''

    def get_all_titles(self, response):
        article_titles = response.xpath(self.xpath_expression).getall()
        return self.get_trimmed_list(article_titles)

    def get_trimmed_list(self, list):
        result = []
        for el in list:
            el = el.replace('\n', '')
            el = el.strip()
            if el != '':
                result.append(el)

        return result
