# NewsScraper - Scrape any newspaper automatically

This is a simple python script for automatically scraping the most recent articles from any news-site.

Just add the websites you want to scrape to `NewsPapers.json` and the script will go through and scrape each site listed in the file.

## Install

```
pip install -r requirements.txt
```

## Usage

Simply run `python newsscraper.py News.json`.


The `NewsPapers.json` file should be a JSON file like this:

```json
{
  "bbc": {
    "rss": "http://feeds.bbci.co.uk/news/rss.xml",
    "link": "http://www.bbc.com/"
  },
  "cnn": {
    "rss": "http://rss.cnn.com/rss/edition.rss",
    "link": "http://edition.cnn.com/"
  },
  "foxnews": {
    "rss": "http://feeds.foxnews.com/foxnews/latest",
    "link": "http://www.foxnews.com/"
  }
}
```


## Libraries

This script uses the following libraries:

https://github.com/codelucas/newspaper

https://github.com/kurtmckee/feedparser
