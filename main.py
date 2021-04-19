#!/usr/bin/env python

from scraper import scrape
from roadrunner import roadrunner
from webstemmer import webstemmer
import time
from constants import FOLDER_NAMES

def main():
    print('Scraping started')
    scrape()
    print('Scraping finished\nRoadrunner started\n')
    rr_start = time.time()
    roadrunner()
    rr_end = time.time()
    print('Roadrunner finished\nWebstemmer started\n')
    webstemmer()
    ws_end = time.time()
    print('\nWebstemmer finished\n\n')

    print('Execution time:\nRoadRunner average time per webpage: {0}s\nWebstemmer average time per webpage: {1}\n'
    .format((rr_end-rr_start)/len(FOLDER_NAMES), (ws_end-rr_end)/len(FOLDER_NAMES)))
    
if __name__ == "__main__":
    main()
