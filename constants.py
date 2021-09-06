# to add a new cluster of websites to analyse, create a list of urls and add:
# - the folder name to the FOLDER_NAMES list
# - the list of urls to the URL_LISTS list


# 24ur
URLS_24_UR = [
    'https://www.24ur.com/tv-oddaje/',
    'https://www.24ur.com/novice/',
    'https://www.24ur.com/sport/',
    'https://www.24ur.com/popin/',
    'https://www.24ur.com/tv-oddaje/',
]

# zurnal
URLS_ZURNAL = [
    'https://www.zurnal24.si/sport/',
    'https://www.zurnal24.si/slovenija/',
    'https://www.zurnal24.si/avto/',
    'https://www.zurnal24.si/zdravje/',
    'https://www.zurnal24.si/magazin/',
]

# delo
URLS_DELO = [
    'https://www.delo.si/novice/',
    'https://www.delo.si/gospodarstvo/',
    'https://www.delo.si/lokalno/',
    'https://www.delo.si/mnenja/',
    'https://www.delo.si/sport/',
]

# rtvslo
URLS_RTVSLO = [
    'https://www.rtvslo.si/sport/',
    'https://www.rtvslo.si/svet/',
    'https://www.rtvslo.si/slovenija/',
    'https://www.rtvslo.si/kultura/',
    'https://www.rtvslo.si/svet-zabave/',
]

# slovenskenovice
URLS_SLOVENSKE_NOVICE = [
    'https://www.slovenskenovice.si/novice/',
    'https://www.slovenskenovice.si/sport/',
    'https://www.slovenskenovice.si/bulvar/',
    'https://www.slovenskenovice.si/kronika/',
    'https://www.slovenskenovice.si/stil/',
]


FOLDER_NAMES = [
    '24ur',
    'zurnal',
    'delo',
    'rtvslo',
    'slovenskenovice',
]


URL_LISTS = [
    URLS_24_UR,
    URLS_ZURNAL,
    URLS_DELO,
    URLS_RTVSLO,
    URLS_SLOVENSKE_NOVICE,
]

import os
SCRAPE_DEST_FOLDER = os.getenv('SCRAPE_DEST_FOLDER', '.')
# add slash if not present
if SCRAPE_DEST_FOLDER[-1] != '/':
    SCRAPE_DEST_FOLDER += '/'