import subprocess
import os

def scrapy():    
    os.chdir("scrapynews")
    subprocess.run('bash customcmds.sh', shell=True, check=True)    
    os.chdir("..")