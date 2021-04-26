# !/bin/bash

scrapy crawl delo -O scraped-content/delo.json -a save-files=True
scrapy crawl rtv -O scraped-content/rtv.json -a save-files=True
scrapy crawl zurnal -O scraped-content/zurnal.json -a save-files=True
scrapy crawl 24ur -O scraped-content/24ur.json -a save-files=True
scrapy crawl slovenske-novice -O scraped-content/slovenske-novice.json -a save-files=True
