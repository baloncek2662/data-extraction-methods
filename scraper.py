# This file writes the HTML of selected pages into the specified folder
# Modify constants.py to customize source pages

import requests
import shutil
import os

from pathlib import Path

from lxml import html
from constants import URL_LISTS, FOLDER_NAMES, SCRAPE_DEST_FOLDER


def scrape():
    for i in range(len(URL_LISTS)):
        write_pages(URL_LISTS[i], FOLDER_NAMES[i])


def write_pages(full_urls, folder_name):
    # clean and prepare folder where we will write our results
    remove_path = Path(SCRAPE_DEST_FOLDER + folder_name)
    if remove_path.exists() and remove_path.is_dir():
        shutil.rmtree(remove_path)

    path = SCRAPE_DEST_FOLDER + folder_name + "/" + folder_name + "/"
    Path(path).mkdir(parents=True, exist_ok=True)  # creates directory

    for full_url in full_urls:
        # we need to pass headers as a workaround for rtvslo, as it returns 410 without it
        # this makes the program much slower though!!
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0",
        }
        response = requests.get(full_url, headers=headers)
        # requests guesses the wrong encoding so we have to fix that
        response.encoding = "utf-8"

        # follow links to actual articles
        response_html = html.fromstring(response.content)
        all_article_urls = response_html.xpath("//a/@href")
        article_urls = get_article_urls(full_url, all_article_urls, folder_name)
        # get response for each article_url and write it to file
        last_category = ""
        count = 0
        for article_url in article_urls:
            article_response = requests.get(article_url, headers=headers)
            article_response.encoding = "utf-8"
            url_slashes_count = (
                3 if folder_name == "24ur" or folder_name == "zurnal" else 4
            )
            category = article_url.split("/")[-url_slashes_count]
            with open(f"{path}{folder_name}_{category}_{count}.html", "w") as file:
                file.write(article_response.text)
            if last_category != category:
                count = 0
            last_category = category
            count += 1

    # creates zip, needed by webstemmer
    cwd = os.getcwd()
    os.chdir(SCRAPE_DEST_FOLDER)
    shutil.make_archive(folder_name, "zip", folder_name)
    os.chdir(cwd)


def get_article_urls(full_url, all_article_urls, folder_name):
    # we judge relevant urls by the number of slashes
    # for 24ur and zurnal the correct number is 3
    #   /sport/nogomet/nekdanji-francoski-nogometas-umrl-po-39-letih-v-komi.html
    # for the others (delo, rtv, slovenskenovice) the correct number is 4:
    #   /sport/drugi-sporti/gajser-tekmecem-pokazal-iz-kaksnega-testa-so-sampioni/
    category = full_url.split("/")[-2]
    url_slashes_count = 3 if folder_name == "24ur" or folder_name == "zurnal" else 4
    partial_article_urls = [
        u
        for u in all_article_urls
        if u.startswith(f"/{category}/") and u.count("/") == url_slashes_count
    ]
    root_url = "/".join(full_url.split("/")[0:-2])  # this gets just the root url
    full_article_urls = [root_url + au for au in partial_article_urls]
    return full_article_urls
