# Data Extraction Methods

A runner of automatic data extraction methods <cite>[RoadRunner][1]</cite> and <cite>[Webstemmer][2]</cite>, as well as a semi-automatic method of extracting data using <cite>[XPath][5]</cite> with the help of the framework <cite>[Scrapy][4]</cite>. Works on news articles. Once your environment is set up, you may run all methods at once by running the executable Python script:

```
$ ./main.py
```

`main.py` runs four functions:
1. `scrape()`, which downloads the HTML from desired webpages into a chosen destination folder (see SCRAPE_DEST_FOLDER below) and creates a zip of them for Webstemmer to use. The destination folder is named `scraped_folders`. As we sometimes want the corpus to stay constant an environment variable `ENABLE_WEB_SCRAPING` may be set to false inside the `.env` file. In addition to the scraped websites, we also create 'mixed' groups which contain HTML and zip files from different websites to see how the methods perform on pages which are not similar to one another. The `scraped-folders` folder must be synced with the FOLDER_NAMES constant in `constants.py`. The exact corpus which is used as an example for this work is available for download at: [https://drive.google.com/file/d/1podWDM7qokj7Wn7-hS-yAPpOVX5nl6_3/view?usp=sharing](https://github.com/baloncek2662/data-extraction-methods/tree/main/constant_scraped_folders)
2. `roadrunner()`, which executes the <cite>[RoadRunner][1]</cite> method and saves results and generated wrappers (in the form of `*.html` and `.*xml` files) into `./roadrunner/output/`
3. `webstemmer()`, which executes the <cite>[Webstemmer][2]</cite> method and saves results (in the form of `*.txt` files) and generated wrappers (in the form of `*.pat` files) into `./webstemmer/webstemmer/`
4. `scrapy()`, which executes a custom implementation of <cite>[Scrapy][4]</cite>, a web crawler that extracts data using <cite>[XPath][5]</cite>, and writes the results into `*.json` files in `./scrapynews/scraped-content/`

In the end the information of time needed per webpage for each data extraction method is shown.


### Environment Setup

- Add URLs to `constants.py` to choose custom webpages from which data will be extracted and the folder names into which they will be extracted. The folder names and URLs indices must correspond
- Create a new file `.env` in the same folder as `main.py` and add the absoulte path of the folder in which you wish to save scraped data to the SCRAPE_DEST_FOLDER environment variable, eg. `SCRAPE_DEST_FOLDER="/home/scraped-folders/"`. You may also set `ENABLE_WEB_SCRAPING` to False if you wish to prevent web scraping in the `scrape` function.
- Initialize <cite>[pipenv][3]</cite> by running `pipenv install`
- Open pipenv shell by running `pipenv shell`
- Add the repository folder to the bash PATH variable since the committed `geckodriver` binary is needed by Selenium to compare results. The executable is downloaded from the <cite>[geckodriver GitHub page][6]</cite>. This is done by running:
`PATH=${PATH}:$(pwd)` in your bash terminal when located inside the repository's root folder.
- Run the program by running `./main.py` from the repository's root folder



[1]: http://www.dia.uniroma3.it/db/roadRunner/software.html
[2]: http://www.unixuser.org/~euske/python/webstemmer/
[3]: https://pypi.org/project/pipenv/
[4]: https://scrapy.org/
[5]: https://developer.mozilla.org/en-US/docs/Web/XPath
[6]: https://github.com/mozilla/geckodriver/releases/download/v0.32.0/geckodriver-v0.32.0-linux64.tar.gz
