#!/usr/bin/env python

import time


from scraper import scrape
from exec_roadrunner import roadrunner
from exec_webstemmer import webstemmer
from exec_scrapynews import scrapynews
from compare_results import compare

from constants import FOLDER_NAMES, ENABLE_WEB_SCRAPING


def main():
    # Always run scraping unless the ENABLE_WEB_SCRAPING variable in .env is set to False
    if ENABLE_WEB_SCRAPING:
        scrape()
    else:
        print("Skipping web scraping")

    start = time.time()
    roadrunner()
    rr_end = time.time()
    webstemmer()
    ws_end = time.time()
    scrapynews()
    scrapy_end = time.time()

    print("Execution times:")
    print(f"RoadRunner average time per webpage: {(rr_end-start)/len(FOLDER_NAMES)}s")
    print(f"Webstemmer average time per webpage: {(ws_end-rr_end)/len(FOLDER_NAMES)}s")
    print(f"Scrapy average time per webpage: {(scrapy_end-ws_end)/len(FOLDER_NAMES)}s")
    print()

    compare()


if __name__ == "__main__":
    main()
