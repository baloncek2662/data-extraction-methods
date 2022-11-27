import os
import time

from constants import FOLDER_NAMES, SCRAPE_DEST_FOLDER


def print_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print(
            f"\nExecution time: [{time.time() - start}] seconds, "
            f"average per website: [{(time.time() - start)/len(FOLDER_NAMES)}] seconds\n"
        )

    return wrapper


def get_webpage_articles_cnt(webpage):
    return len(os.listdir(f"{SCRAPE_DEST_FOLDER}{webpage}/{webpage}"))


def get_articles_cnt():
    articles_cnt = {"all": 0}
    for webpage in FOLDER_NAMES:
        webpage_articles_cnt = get_webpage_articles_cnt(webpage)
        articles_cnt["all"] += webpage_articles_cnt
        articles_cnt[webpage] = webpage_articles_cnt
    return articles_cnt
