# !/bin/bash

readonly BASE_PATH=$(pwd)
export PYTHONPATH=$PYTHONPATH:BASE_PATH/../../

SPIDER_NAMES=('delo' 'rtvslo' 'zurnal' '24ur' 'slovenskenovice')

for SPIDER in $SPIDER_NAMES 
do
    scrapy crawl $SPIDER -O scraped-content/$SPIDER.json -a save-files=True  -s LOG_ENABLED=False
done