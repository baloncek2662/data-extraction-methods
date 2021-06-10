# ./roadrunner/output/*.???
# ./webstemmer/webstemmer/*.txt
# ./scrapynews/scraped-content/*.json

import json
from constants import FOLDER_NAMES
from pathlib import Path
import csv


def compare():
    webstemmer_titles = get_webstemmer_titles()
    scrapy_titles = get_scrapy_titles()
    print(f'Number of titles scraped by scrapy: {get_total_titles_len(scrapy_titles)}')
    print(f'Number of titles scraped by webstemmer: {get_total_titles_len(webstemmer_titles)}')

    generate_csv(scrapy_titles, 'scrapy')
    generate_csv(webstemmer_titles, 'webstemmer')



def get_roadrunner_titles():
    '''
    Result format:
    '''


def get_webstemmer_titles():
    '''
    Result format:
    [
        {'24ur': [...DATA...]},
        
    ]
    '''
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
    '''
    Result format:
    [
        {'24ur': [...DATA...]},
        
    ]
    '''
    result = []
    for webpage in FOLDER_NAMES:
        webpage_titles = {}
        with open(f'./scrapynews/scraped-content/{webpage}.json', 'r') as file:
            webpage_titles = json.load(file)
        # webpage_titles is an array of 5 objects: {'webpage': [...DATA...]}
        # we need to combine them into a single object: {'webpage': [...DATA...]},
        titles_list = []
        for section in webpage_titles:
            section_titles_list = section[webpage]
            titles_list.extend(section_titles_list)

        result.append({webpage : titles_list})


    
    return result


def get_total_titles_len(titles_list):
    result = 0
    for title_dict in titles_list:
        for webpage in title_dict: # there is only webpage, but this is still the easiest option to count it
            result += len(title_dict[webpage])
    return result


def generate_csv(titles_list, csv_name):
    '''
    Generate a csv with 5 columns, one for each webpage.
    All the webpage's titles are in the same column 
    Input format (titles_list) must be:
    [
        {'24ur': [...DATA...]},
        
    ]
    '''
    Path("./results").mkdir(parents=True, exist_ok=True)
    with open(f'./results/{csv_name}.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
        first_row = get_first_csv_row()
        csv_writer.writerow(first_row)
    
        row_count = 0
        no_more_rows = False
        while not no_more_rows:
            csv_row = []
            no_more_rows = True
            for title_dict in titles_list: 
                for webpage in title_dict: # there is only webpage
                    webpage_titles_list = title_dict[webpage]
                    if len(webpage_titles_list) <= row_count: # if no more rows left for this webpage, append empty space
                        csv_row.append(' ') 
                    else: # else append the title
                        csv_row.append(webpage_titles_list[row_count])
                        no_more_rows = False
                    csv_row.append(' ') # always append an empty space as the delimited
            csv_row = csv_row[:-1] # delete last empty space
            csv_writer.writerow(csv_row)
            row_count += 1



def get_first_csv_row():
    result = []
    for folder in FOLDER_NAMES:
        result.append(folder)
        result.append(' ')
    result = result[:-1] # delete last empty space
    return result