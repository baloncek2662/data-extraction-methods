# to add a new cluster of websites to analyse, create a list of urls and add:
# - the folder name to the FOLDER_NAMES list
# - the list of urls to the URL_LISTS list

import os

# 24ur
URLS_24_UR = [
    "https://www.24ur.com/magazin/",
    "https://www.24ur.com/novice/",
    "https://www.24ur.com/sport/",
    "https://www.24ur.com/popin/",
    "https://www.24ur.com/tv-oddaje/",
]

# zurnal
URLS_ZURNAL = [
    "https://www.zurnal24.si/sport/",
    "https://www.zurnal24.si/pod-streho/",
    "https://www.zurnal24.si/avto/",
    "https://www.zurnal24.si/zdravje/",
    "https://www.zurnal24.si/magazin/",
]

# delo
URLS_DELO = [
    "https://www.delo.si/novice/",
    "https://www.delo.si/gospodarstvo/",
    "https://www.delo.si/lokalno/",
    "https://www.delo.si/mnenja/",
    "https://www.delo.si/sport/",
]

# rtvslo
URLS_RTVSLO = [
    "https://www.rtvslo.si/sport/",
    "https://www.rtvslo.si/svet/",
    "https://www.rtvslo.si/zabava-in-slog/",
    "https://www.rtvslo.si/kultura/",
    "https://www.rtvslo.si/lokalne-novice/",
]

# slovenskenovice
URLS_SLOVENSKE_NOVICE = [
    "https://www.slovenskenovice.si/novice/",
    "https://www.slovenskenovice.si/sport/",
    "https://www.slovenskenovice.si/bulvar/",
    "https://www.slovenskenovice.si/kronika/",
    "https://www.slovenskenovice.si/stil/",
]


URL_LISTS = {
    "24ur": URLS_24_UR,
    "zurnal": URLS_ZURNAL,
    "delo": URLS_DELO,
    "rtvslo": URLS_RTVSLO,
    "slovenskenovice": URLS_SLOVENSKE_NOVICE,
}


FOLDER_NAMES = [
    "24ur",
    "zurnal",
    "delo",
    "rtvslo",
    "slovenskenovice",
    # Scraping not implemented for below folders! Only run program with scraping
    # enabled if the folders are commented out!
    # "slovenskenovice-delo",
    # "zurnal-24ur",
    # "24ur-zurnal-delo",
    # "all_mixed",
]


# Roadrunner fails to generate a wrapper for the following websites, meaning we must
# skip their analysis or else the program will crash.
ROADRUNNER_WRAPPER_FAIL = ["slovenskenovice", "rtvslo", "zurnal-24ur", "24ur-zurnal-delo", "all_mixed"]


SCRAPE_DEST_FOLDER = os.getenv("SCRAPE_DEST_FOLDER", ".")
# add slash if not present
if SCRAPE_DEST_FOLDER[-1] != "/":
    SCRAPE_DEST_FOLDER += "/"


ENABLE_WEB_SCRAPING = False if os.getenv("ENABLE_WEB_SCRAPING") == "False" else True
