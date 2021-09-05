# this file writes the HTML of selected 
# pages into the specified folder
# modify constants.py to customize source pages

import requests
import shutil
import os

from pathlib import Path
from lxml import html
from constants import URL_LISTS, FOLDER_NAMES, SCRAPE_DEST_FOLDER

def scrape():
    for i in range(len(URL_LISTS)):
        responses = get_url_responses(URL_LISTS[i])
        write_pages(responses, FOLDER_NAMES[i])


def write_pages(pages, folder_name):
    # requests guesses the wrong encoding so we have to fix that
    for page in pages:
        page.encoding = 'utf-8'

        # tmp workaround, rtv returns 410 status atm
        if folder_name == 'rtvslo':
            break

        # follow links to actual articles
        page_html = html.fromstring(pages[0].content)
        all_urls = page_html.xpath('//a/@href')
        article_urls = get_article_urls(all_urls, folder_name)

    remove_path = Path(SCRAPE_DEST_FOLDER + folder_name)
    if remove_path.exists() and remove_path.is_dir():
        shutil.rmtree(remove_path)

    path = SCRAPE_DEST_FOLDER + folder_name + '/' + folder_name + '/'
    Path(path).mkdir(parents=True, exist_ok=True) # creates directory
    
    for i in range(len(pages)):
        with open(path + str(i) +'.html', 'w') as file:
            file.write(pages[i].text)

    # creates zip, needed by webstemmer
    cwd = os.getcwd()
    os.chdir(SCRAPE_DEST_FOLDER)
    shutil.make_archive(folder_name, 'zip', folder_name)
    os.chdir(cwd)


def get_url_responses(url_list):
    result = []
    for url in url_list:
        result.append(requests.get(url))
    return result

def get_article_urls(all_urls, folder_name):
    # we judge relevant urls by the number of slashes
    # for 24ur and zurnal the correct number is 3
    # for the others (delo, rtv, slovenskenovice) the correct number is 4: 
    # /sport/drugi-sporti/gajser-tekmecem-pokazal-iz-kaksnega-testa-so-sampioni/ 
    url_slashes_count = 3 if folder_name == '24ur' or folder_name == 'zurnal' else 4
    article_urls = [u for u in all_urls if u.startswith('/sport/') and u.count('/') == url_slashes_count]
    print(article_urls)
