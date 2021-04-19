# Data Extraction Methods

An automatic runner of data extraction methods RoadRunner and Webstemmer. Works on news articles. Once your environment is set up, you may run both methods at once by running the executable Python script:

```
$ ./main.py
```

`main.py` runs three functions:
1. `scrape()`, which downloads the HTML from desired webpages into `./examples/` and creates a zip of them for Webstemmer to use 
2. `roadrunner()`, which executes the <cite>[RoadRunner][1]</cite> method and saves results into `./roadrunner/output/`
3. `webstemmer()`, which executes the <cite>[Webstemmer][2]</cite> method and saves results (in the form of `*.txt` files) and generated wrappers (in the form of `*.pat` files) into `./webstemmer/webstemmer/` 

In the end the information of time needed per webpage for each data extraction method is shown.


### Environment Setup

- Add URLs to `constants.py` to choose custom webpages from which data will be extracted
- Create a new file `.env` in the same folder as `main.py` and add the absoulte path of the folder in which you wish to save scraped data to the SCRAPE_DEST_FOLDER environment variable, eg. ` 
SCRAPE_DEST_FOLDER="/home/scraped-folders/"`
- Initialize <cite>[pipenv][3]</cite> by running `pipenv install` 
- Open pipenv shell by running `pipenv shell`
- Run the program by running `./main.py`



[1]: http://www.dia.uniroma3.it/db/roadRunner/software.html
[2]: http://www.unixuser.org/~euske/python/webstemmer/
[3]: https://pypi.org/project/pipenv/