import os
import subprocess
import time

from constants import FOLDER_NAMES, SCRAPE_DEST_FOLDER


def webstemmer():
    for folder in FOLDER_NAMES:
        analyse_pages(folder)


def analyse_pages(folder_name):
    os.chdir("webstemmer/webstemmer")

    start_time = time.time()

    analyse_command = "./analyze.py"
    # options
    analyse_command += " -t 0.5 -S 1"
    # html src
    analyse_command += " " + SCRAPE_DEST_FOLDER + folder_name + ".zip"
    # layout pattern destination file
    analyse_command += " > " + folder_name + "_WS" + ".pat"
    subprocess.run(analyse_command, shell=True, check=True)

    extract_command = "./extract.py"
    # options
    extract_command += " -t 0.5 -T 0.7 -M 20"
    # layout analysis file and html source
    extract_command += (
        " " + folder_name + "_WS" + ".pat " + SCRAPE_DEST_FOLDER + folder_name + ".zip"
    )
    # results destination file
    extract_command += " > " + folder_name + "_WS" + ".txt"
    subprocess.run(extract_command, shell=True, check=True)

    print("\nExecution time: {:.2f}s".format(time.time() - start_time))

    os.chdir("../..")

    print("--------------------------------------------\n")
