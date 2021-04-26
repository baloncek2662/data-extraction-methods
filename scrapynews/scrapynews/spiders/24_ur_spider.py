import scrapy

spider_name = '24ur'

class Spider24ur(scrapy.Spider):
    name = spider_name
    save_files=False

    def start_requests(self):
        save_files_attr = getattr(self, 'save-files', None)
        if save_files_attr == 'True':
            self.save_files = True
            
        # TODO import from ../../../constants.py - URLS_24_UR
        urls = [
            'https://www.24ur.com/',
            'https://www.24ur.com/novice',
            'https://www.24ur.com/sport',
            'https://www.24ur.com/popin',
            'https://www.24ur.com/tv-oddaje',
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
        article_titles = response.xpath('//span[has-class("card__title-inside")]/text()').getall()
        print(article_titles)
        return self.get_trimmed_list(article_titles)

    def get_trimmed_list(self, l):
        result = []
        for el in l:
            el = el.replace('\n', '')
            el = el.strip()
            if el != '':
                result.append(el)

        return result

        #<h1 class="card-overlay__title card-overlay__title--large">Mavericksi so h Kingsom prišli po povračilo</h1>
        #<h1 class="card-overlay__title">Lazio ugnal Milan na derbiju, Napoli prehitel Juventus</h1>
        #<h2 class="card__title card__title--small"><span class="card__title-inside">City pred osem tisoč navijači do zmage v ligaškem pokalu, le točka Uniteda v ...</span></h2>
        #<span class="card__title-inside">Zidane: Dovolj je vprašanj o Superligi, zanimata me le Liga prvakov in Chelsea</span>