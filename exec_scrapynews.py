import subprocess
import os
import time

from constants import FOLDER_NAMES
from utils import print_time


@print_time
def scrapynews():
    print("===== Scrapynews started =====\n")

    os.chdir("scrapynews")

    for folder in FOLDER_NAMES:
        start = time.time()
        analyse_pages(folder)
        print(f"Execution time for {folder}: [{time.time() - start}] seconds\n")

    os.chdir("..")


def analyse_pages(folder_name):
    print(f"Running scrapynews on folder {folder_name}\n")

    command = f"scrapy crawl {folder_name} -O results/{folder_name}_SN.json"
    # options to avoid log spamming and duplicate saving of html files
    command += " -a save-files=False -s LOG_ENABLED=False"

    subprocess.run(command, shell=True, check=True)
