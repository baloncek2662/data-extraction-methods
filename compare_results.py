# ./roadrunner/output/{webpage}/{webpage}0_DataSet.xml
# ./webstemmer/webstemmer/{webpage}.txt
# ./scrapynews/scraped-content/{webpage}.json

import json
from constants import FOLDER_NAMES
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils import get_articles_cnt


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

    articles_cnt = get_articles_cnt()

    print_results_len(roadrunner_results, articles_cnt, rr_end - start, "Roadrunner")
    print_results_len(webstemmer_results, articles_cnt, ws_end - rr_end, "Webstemmer")
    print_results_len(scrapy_results, articles_cnt, scrapy_end - ws_end, "Scrapy")

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
        # rtv blocks execution due to error with generating wrapper
        if webpage == "rtvslo":
            continue

        driver = webdriver.Firefox()
        driver.get(
            f"file://{os.getcwd()}/roadrunner/output/{webpage}_RR/{webpage}_RR0_DataSet.xml"
        )
        webpage_titles = driver.find_elements(
            By.XPATH, "/html/body/table/tbody/tr[2]/td/table/tbody/tr[2]/td[1]/div/div"
        )
        webpage_titles = [
            title.text for title in webpage_titles if title.text != "null"
        ]

        # Roadrunner does not produce a standardized format of subtitles and contents so we leave
        # these fields empty.
        webpage_results = {
            "titles": webpage_titles,
            "subtitles": [],
            "contents": [],
        }

        result.append({webpage: webpage_results})

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
    # Subtitles and content are found in lines starting with "SUB-xx: " and "MAIN-xx: "
    TITLE_STR, SUBTITLE_STR, CONTENT_STR = "TITLE: ", "SUB", "MAIN"
    for webpage in FOLDER_NAMES:
        webpage_titles, webpage_subtitles, webpage_contents = [], [], []
        article_subtitle, article_content = "", ""
        with open(f"./webstemmer/webstemmer/{webpage}_WS.txt", "r") as file:
            lines = [line.rstrip() for line in file]
            for line in lines:
                # Subtitles and main content are split into several lines, so we combine them into a single
                # string and then add it to the list. The string is reset whenever an empty line is found since
                # that means that the next batch of lines belongs to a new article.
                if line == "":
                    if article_subtitle.rstrip() != "":
                        webpage_subtitles.append(article_subtitle.rstrip())
                    if article_content.rstrip() != "":
                        webpage_contents.append(article_content.rstrip())
                    article_subtitle, article_content = "", ""

                if line.startswith(TITLE_STR):
                    webpage_titles.append(line.split(":")[1].rstrip())
                elif line.startswith(SUBTITLE_STR):
                    article_subtitle += f"{line.split(': ')[1].rstrip()} "
                elif line.startswith(CONTENT_STR):
                    article_content += f"{line.split(': ')[1].rstrip()} "

        webpage_results = {
            "titles": webpage_titles,
            "subtitles": webpage_subtitles,
            "contents": webpage_contents,
        }

        result.append({webpage: webpage_results})

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
        webpage_titles, webpage_subtitles, webpage_contents = [], [], []
        for article in scrapy_json:
            article_title = article[webpage]["title"]
            article_subtitle = article[webpage]["subtitle"]
            article_content = article[webpage]["content"]
            if article_title is not None:
                webpage_titles.append(article_title.rstrip())
            if article_subtitle is not None:
                webpage_subtitles.append(article_subtitle.rstrip())
            if article_content is not None:
                webpage_contents.append(article_content.rstrip())

        webpage_results = {
            "titles": webpage_titles,
            "subtitles": webpage_subtitles,
            "contents": webpage_contents,
        }

        result.append({webpage: webpage_results})

    return result


def print_results_len(results_list, articles_cnt, time, method):
    result = {"titles": 0, "subtitles": 0, "contents": 0}
    print()
    print(f"======= {method} =======")
    for result_dict in results_list:
        # there is only webpage, but this is still the easiest option to count it
        for webpage in result_dict:
            for key in ["titles"]:
                result_key_len = len(result_dict[webpage][key])
                percentage = round(result_key_len / articles_cnt[webpage] * 100, 2)
                print(
                    f"Webpage [{webpage:15s}] scraped [{str(result_key_len).zfill(2)}] [{key:9s}], "
                    f"accuracy was {percentage}%"
                )
                result[key] += result_key_len

    all_titles_percentage = round(result['titles'] / articles_cnt['all'] * 100, 2)
    all_subtitles_percentage = round(result['subtitles'] / articles_cnt['all'] * 100, 2)
    all_contents_percentage = round(result['contents'] / articles_cnt['all'] * 100, 2)

    print(f"Total articles count: [{articles_cnt['all']}]")
    print(f"{method} titles scraped: [{result['titles']}] ({all_titles_percentage}%)")
    print(f"{method} subtitles scraped: [{result['subtitles']}] ({all_subtitles_percentage * 100:.4}%)")
    print(f"{method} contents scraped: [{result['contents']}] ({all_contents_percentage * 100:.4}%)")
    print(
        f"{method} scraped [{result}] for a total of "
        f"[{result['titles'] + result['subtitles'] + result['contents']}] results. "
        f"Comparsion method took [{time}] seconds"
    )


def generate_csv(webpages_dict_list, csv_name):
    """
    Generate a csv with 5 columns, one for each webpage.
    All the webpage's categories are in the same column
    Input format (category_list) must be:
    [
        {'webpage': [{'category': [...DATA...]} ]},

    ]
    """
    Path("./results").mkdir(parents=True, exist_ok=True)
    for category in ["titles"]:
        with open(f"./results/{csv_name}_{category}.csv", "w", newline="") as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=",", quoting=csv.QUOTE_ALL)
            first_row = get_first_csv_row()
            csv_writer.writerow(first_row)

            row_count = 0
            no_more_rows = False
            while not no_more_rows:
                csv_row = []
                no_more_rows = True
                for webpage_dict in webpages_dict_list:
                    for webpage in webpage_dict:  # there is only webpage
                        webpage_category_list = webpage_dict[webpage][category]
                        if (
                            len(webpage_category_list) <= row_count
                        ):  # if no more rows left for this webpage, append empty space
                            csv_row.append(" ")
                        else:  # else append the title
                            csv_row.append(webpage_category_list[row_count])
                            no_more_rows = False
                        # always append an empty space as the delimiter
                        csv_row.append(" ")
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
