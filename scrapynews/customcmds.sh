#!/bin/bash

BASE_PATH=$(pwd)
export PYTHONPATH=$PYTHONPATH:$BASE_PATH/../

SPIDER_NAMES=('delo' 'rtvslo' 'zurnal' '24ur' 'slovenskenovice')

for SPIDER in "${SPIDER_NAMES[@]}"
do
    echo "Running spider: ${SPIDER}"
    scrapy crawl "$SPIDER" -O scraped-content/"${SPIDER}"_SN.json -a save-files=False -s LOG_ENABLED=False
done
