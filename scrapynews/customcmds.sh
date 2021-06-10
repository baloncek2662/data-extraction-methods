# !/bin/bash

readonly BASE_PATH=$(pwd)
export PYTHONPATH=$PYTHONPATH:BASE_PATH/../../

scrapy crawl delo -O scraped-content/delo.json -a save-files=True
scrapy crawl rtvslo -O scraped-content/rtvslo.json -a save-files=True
scrapy crawl zurnal -O scraped-content/zurnal.json -a save-files=True
scrapy crawl 24ur -O scraped-content/24ur.json -a save-files=True
scrapy crawl slovenskenovice -O scraped-content/slovenskenovice.json -a save-files=True
