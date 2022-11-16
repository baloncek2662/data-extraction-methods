import subprocess
import os


def scrapynews():
    os.chdir("scrapynews")
    subprocess.run("bash customcmds.sh", shell=True, check=True)
    os.chdir("..")
