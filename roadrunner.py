import subprocess
import os
import glob
import time

from constants import FOLDER_NAMES, SCRAPE_DEST_FOLDER


def roadrunner():
    for folder in FOLDER_NAMES:
        analyse_pages(folder)


def analyse_pages(folder_name):
    # base java command
    command = "java -cp lib/roadrunner.jar:lib/nekohtml.jar:lib/xercesImpl.jar:lib/xmlParserAPIs.jar roadrunner.Shell"
    # output folder located in 'output/folder_name'
    command += f" -N{folder_name}_RR"
    # configuration parameters which will be used
    command += " -Oexamples/prefs.xml"

    pages = glob.glob(f"{SCRAPE_DEST_FOLDER}{folder_name}/{folder_name}/*")
    for page in pages:
        command += " " + page

    os.chdir("roadrunner")

    start_time = time.time()
    subprocess.run(command, shell=True, check=True)
    print("\nExecution time: {:.2f}s".format(time.time() - start_time))

    os.chdir("..")

    print("--------------------------------------------\n")
