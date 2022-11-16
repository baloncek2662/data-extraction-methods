import subprocess
import os
import time

from constants import FOLDER_NAMES


def scrapynews():
    print("===== Scrapynews started =====\n")

    os.chdir("scrapynews")

    for folder in FOLDER_NAMES:
        analyse_pages(folder)

    os.chdir("..")


def analyse_pages(folder_name):
    start_time = time.time()

    print(f"Running scrapynews on folder {folder_name}\n")

    command = f"scrapy crawl {folder_name} -O scraped-content/{folder_name}_SN.json"
    # options to avoid log spamming and duplicate saving of html files
    command += " -a save-files=False -s LOG_ENABLED=False"

    subprocess.run(command, shell=True, check=True)

    print("\nExecution time: {:.2f}s".format(time.time() - start_time))
    print("\n--------------------------------------------\n")
