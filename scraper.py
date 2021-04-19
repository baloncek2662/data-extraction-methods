# =======================
#
# this file writes the HTML of selected 
# pages into the specified folder
#
# =======================

from pathlib import Path
from constants import URL_LISTS, FOLDER_NAMES
import requests
import shutil
import os

def scrape():
    for i in range(len(URL_LISTS)):
        responses = get_url_responses(URL_LISTS[i])
        write_pages(responses, FOLDER_NAMES[i])


def write_pages(pages, folder):
    # requests guesses the wrong encoding so we have to fix that
    for page in pages:
        page.encoding = 'utf-8'

    remove_path = Path('examples/' + folder)
    if remove_path.exists() and remove_path.is_dir():
        shutil.rmtree(remove_path)

    path = 'examples/' + folder + '/' + folder + '/'
    Path(path).mkdir(parents=True, exist_ok=True) # creates directory
    
    for i in range(len(pages)):
        with open(path + str(i) +'.html', 'w') as file:
            # text = get_body(pages[i])
            # soup = BeautifulSoup(text, 'html.parser')
            file.write(pages[i].text)

    # creates zip, needed by webstemmer
    os.chdir('examples')
    shutil.make_archive(folder, 'zip', folder)
    os.chdir('..')


def get_url_responses(url_list):
    result = []
    for url in url_list:
        result.append(requests.get(url))
    return result

# def get_body(page):
#     result = page.text
#     # result = result.split('</head>')[1]
#     # print(len(result.split('</head>')))
#     return result

# def get_sd_ur_responses():
#     result = []
#     for url in URLS_SD_UR:
#         result.append(requests.get(url))
#     return result

# def get_zurnal_responses():
#     result = []
#     for url in URLS_ZURNAL:
#         result.append(requests.get(url))
#     return result

# def get_delo_responses():
#     result = []
#     for url in URLS_DELO:
#         result.append(requests.get(url))
#     return result