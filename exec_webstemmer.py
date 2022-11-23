import os
import subprocess

from constants import FOLDER_NAMES, SCRAPE_DEST_FOLDER
from utils import print_time


@print_time
def webstemmer():
    print("===== Webstemmer started =====\n")

    os.chdir("webstemmer/webstemmer")

    for folder in FOLDER_NAMES:
        analyse_pages(folder)

    os.chdir("../..")


def analyse_pages(folder_name):
    print(f"Running webstemmer on folder {folder_name}\n")

    analyse_command = "./analyze.py"
    # options
    analyse_command += " -t 0.5 -S 1"
    # html src
    analyse_command += f" {SCRAPE_DEST_FOLDER}{folder_name}.zip"
    # layout pattern destination file
    analyse_command += f" > {folder_name}_WS.pat"
    subprocess.run(analyse_command, shell=True, check=True)

    extract_command = "./extract.py"
    # options
    extract_command += " -t 0.5 -T 0.7 -M 20"
    # layout analysis file and html source
    extract_command += f" {folder_name}_WS.pat {SCRAPE_DEST_FOLDER}{folder_name}.zip"
    # results destination file
    extract_command += f" > {folder_name}_WS.txt"

    subprocess.run(extract_command, shell=True, check=True)
