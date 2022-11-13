# ./roadrunner/output/{webpage}/{webpage}0_DataSet.xml
# ./webstemmer/webstemmer/{webpage}.txt
# ./scrapynews/scraped-content/{webpage}.json

import json
from constants import FOLDER_NAMES
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By


import time
import os
import csv


def compare():
    start = time.time()
    roadrunner_results = get_roadrunner_results()
    rr_end = time.time()
    webstemmer_results = get_webstemmer_results()
    ws_end = time.time()
    scrapy_results = get_scrapy_results()
    scrapy_end = time.time()

    print(
        f"Number of results scraped by roadrunner: {get_total_results_len(roadrunner_results)} in {rr_end-start}s"
    )
    print(
        f"Number of results scraped by webstemmer: {get_total_results_len(webstemmer_results)} in {ws_end-rr_end}s"
    )
    print(
        f"Number of results scraped by scrapy: {get_total_results_len(scrapy_results)} in {scrapy_end-ws_end}s"
    )

    generate_csv(roadrunner_results, "roadrunner")
    generate_csv(webstemmer_results, "webstemmer")
    generate_csv(scrapy_results, "scrapy")


def get_roadrunner_results():
    """
    Result format:
    [
        {'24ur': [...DATA...]},

    ]
    """
    result = []
    for webpage in FOLDER_NAMES:
        # slovenskenovice and rtv block execution due to error with generating wrapper
        if webpage == "slovenskenovice" or webpage == "rtvslo":
            continue

        driver = webdriver.Firefox()
        driver.get(
            f"file://{os.getcwd()}/roadrunner/output/{webpage}_RR/{webpage}_RR0_DataSet.xml"
        )
        webpage_titles = driver.find_elements(
            By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr[2]/td[1]/div/div'
        )
        webpage_titles = [
            title.text for title in webpage_titles if title.text != 'null'
        ]
        result.append({webpage: webpage_titles})

        driver.close()

    return result


def get_webstemmer_results():
    """
    Result format:
    [
        {'24ur': [...DATA...]},

    ]
    """
    result = []
    # Titles in webstemmer output files are found in lines starting with "TITLE: "
    TITLE_STR = "TITLE: "
    for webpage in FOLDER_NAMES:
        webpage_titles = []
        with open(f"./webstemmer/webstemmer/{webpage}_WS.txt", "r") as file:
            lines = [line.rstrip() for line in file]
            for line in lines:
                if line.startswith(TITLE_STR):
                    webpage_titles.append(line[len(TITLE_STR):])
        result.append({webpage: webpage_titles})

    return result


def get_scrapy_results():
    """
    Result format:
    [
        {'24ur': [...DATA...]},

    ]
    """
    result = []
    for webpage in FOLDER_NAMES:
        scrapy_json = {}
        with open(f"./scrapynews/scraped-content/{webpage}_SN.json", "r") as file:
            scrapy_json = json.load(file)
        # scrapy_json is an array of 5 objects: {'webpage': [...DATA...], 'webpage': [...DATA...], ...}
        # we need to combine them into a single object: {'webpage': [...DATA...]},
        webpage_titles = []
        for article in scrapy_json:
            article_title = article[webpage]["title"]
            if article_title is None:
                continue
            webpage_titles.append(article_title.rstrip())
        result.append({webpage: webpage_titles})

    return result


def get_total_results_len(titles_list):
    result = 0
    for title_dict in titles_list:
        # there is only webpage, but this is still the easiest option to count it
        for webpage in title_dict:
            result += len(title_dict[webpage])
    return result


def generate_csv(titles_list, csv_name):
    """
    Generate a csv with 5 columns, one for each webpage.
    All the webpage's titles are in the same column
    Input format (titles_list) must be:
    [
        {'24ur': [...DATA...]},

    ]
    """
    Path("./results").mkdir(parents=True, exist_ok=True)
    with open(f"./results/{csv_name}.csv", "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=",", quoting=csv.QUOTE_ALL)
        first_row = get_first_csv_row()
        csv_writer.writerow(first_row)

        row_count = 0
        no_more_rows = False
        while not no_more_rows:
            csv_row = []
            no_more_rows = True
            for title_dict in titles_list:
                for webpage in title_dict:  # there is only webpage
                    webpage_titles_list = title_dict[webpage]
                    if (
                        len(webpage_titles_list) <= row_count
                    ):  # if no more rows left for this webpage, append empty space
                        csv_row.append(" ")
                    else:  # else append the title
                        csv_row.append(webpage_titles_list[row_count])
                        no_more_rows = False
                    csv_row.append(" ")  # always append an empty space as the delimited
            csv_row = csv_row[:-1]  # delete last empty space
            csv_writer.writerow(csv_row)
            row_count += 1


def get_first_csv_row():
    result = []
    for folder in FOLDER_NAMES:
        result.append(folder)
        result.append(" ")
    result = result[:-1]  # delete last empty space
    return result
