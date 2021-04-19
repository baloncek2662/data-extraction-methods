# this file writes the HTML of selected 
# pages into the specified folder
# modify constants.py to customize source pages

import requests
import shutil
import os

from pathlib import Path
from constants import URL_LISTS, FOLDER_NAMES, SCRAPE_DEST_FOLDER

def scrape():
    for i in range(len(URL_LISTS)):
        responses = get_url_responses(URL_LISTS[i])
        write_pages(responses, FOLDER_NAMES[i])


def write_pages(pages, folder):
    # requests guesses the wrong encoding so we have to fix that
    for page in pages:
        page.encoding = 'utf-8'

    remove_path = Path(SCRAPE_DEST_FOLDER + folder)
    if remove_path.exists() and remove_path.is_dir():
        shutil.rmtree(remove_path)

    path = SCRAPE_DEST_FOLDER + folder + '/' + folder + '/'
    Path(path).mkdir(parents=True, exist_ok=True) # creates directory
    
    for i in range(len(pages)):
        with open(path + str(i) +'.html', 'w') as file:
            # text = get_body(pages[i])
            # soup = BeautifulSoup(text, 'html.parser')
            file.write(pages[i].text)

    # creates zip, needed by webstemmer
    cwd = os.getcwd()
    os.chdir(SCRAPE_DEST_FOLDER)
    shutil.make_archive(folder, 'zip', folder)
    os.chdir(cwd)


def get_url_responses(url_list):
    result = []
    for url in url_list:
        result.append(requests.get(url))
    return result

