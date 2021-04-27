# ./roadrunner/output/*.???
# ./webstemmer/webstemmer/*.txt
# ./scrapynews/scraped-content/*.json

import json
from constants import FOLDER_NAMES

def compare():
    webstemmer_titles = get_webstemmer_titles()
    scrapy_titles = get_scrapy_titles()
    print(scrapy_titles)
    print(webstemmer_titles)

def get_webstemmer_titles():
    result = []
    for webpage in FOLDER_NAMES:
        webpage_titles = []
        with open(f'./webstemmer/webstemmer/{webpage}.txt', 'r') as file:
            for line in file:
                if line[:-1] != '':
                    webpage_titles.append(line[:-1])
        result.append({webpage : webpage_titles})

    return result

def get_scrapy_titles():
    result = []
    for webpage in FOLDER_NAMES:
        webpage_titles = []
        with open(f'./scrapynews/scraped-content/{webpage}.json', 'r') as file:
            webpage_titles = json.load(file)
        result.append({webpage : webpage_titles})

    return result