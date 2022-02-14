#!/usr/bin/env python

import time


from scraper import scrape
from roadrunner import roadrunner
from webstemmer import webstemmer
from scrapy_runner import scrapy
from compare_results import compare

from constants import FOLDER_NAMES

def main():
    #print('Scraping started')
    scrape()
    #print('Scraping finished\nRoadrunner started\n')
    print('Roadrunner started\n')
    start = time.time()
    roadrunner()
    rr_end = time.time()
    print('Roadrunner finished\nWebstemmer started\n')
    webstemmer()
    ws_end = time.time()
    print('\nWebstemmer finished\n\n')
    scrapy()
    scrapy_end = time.time()
    print('\nScrapy finished\n\n')

    print('Execution times:')
    print(f'RoadRunner average time per webpage: {(rr_end-start)/len(FOLDER_NAMES)}s')
    print(f'Webstemmer average time per webpage: {(ws_end-rr_end)/len(FOLDER_NAMES)}s')
    print(f'Scrapy average time per webpage: {(scrapy_end-ws_end)/len(FOLDER_NAMES)}s')
    print()

    compare()
    
if __name__ == "__main__":
    main()
