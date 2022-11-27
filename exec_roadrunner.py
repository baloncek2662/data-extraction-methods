import subprocess
import os
import glob

from constants import FOLDER_NAMES, SCRAPE_DEST_FOLDER
from utils import print_time


@print_time
def roadrunner():
    print("===== Roadrunner started =====\n")

    os.chdir("roadrunner")

    for folder in FOLDER_NAMES:
        analyse_pages(folder)

    os.chdir("..")


def analyse_pages(folder_name):
    print(f"Running roadrunner on folder {folder_name}\n")

    command = "java -cp lib/roadrunner.jar:lib/nekohtml.jar:lib/xercesImpl.jar:lib/xmlParserAPIs.jar roadrunner.Shell"
    # output folder located in 'output/{folder_name}_RR'
    command += f" -N{folder_name}_RR"
    # configuration parameters which will be used
    command += " -Oconfigs/prefs.xml"

    pages = glob.glob(f"{SCRAPE_DEST_FOLDER}{folder_name}/{folder_name}/*")
    for page in pages:
        command += " " + page

    subprocess.run(command, shell=True, check=True)
