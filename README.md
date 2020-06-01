# LWR News Scraper

## Purpose

The purpose of this program is to fetch news articles from the following news pages in the LWR website:
- https://www.livestockwaterrecycling.com/newsroom/featured.html
- https://www.livestockwaterrecycling.com/newsroom/press.html

The reason these news articles are being extracted is to utlimately show news in the LWR mobile android/ios application:
- [Application Repository](https://github.com/LivestockWaterRecycling/ipad-android-mobile-application)

## General Information

- This repository should be public, as we can treat the output .json files the script produces as a nomal JSON API.
- This means we can access these .json files through a url, such as: 

   __articles.json__: https://github.com/LivestockWaterRecycling/lwr-news-scraper/blob/master/articles.json

- Ultimately, we want to configure this script to run every couple of days or so in order for the data to stay updated. This process can be automated by creating a bash script to launch the program and automating a commit and push to the repository.

## Getting Started

### Dependencies

- Make sure you have python 3.5 or above to ensure proper installation of scrappy.

- As you can guess, in order to be able to use this program you must have [scrapy](https://scrapy2.readthedocs.io/en/latest/#) installed.
You can follow [this guide](https://docs.scrapy.org/en/latest/intro/install.html) to download scrapy if you have not used it before.



### Important Files

If you ever need to edit the code that actually scrapes the data, the assosciated python file is located in lwr_news_scraper/spiders/... 

The spiders folder contains all the crawlers in this project. In our case, it contains two: 
* __lwr_spider_press.py__
* __lwr_spider_featured.py__

The reason we need two different spiders/crawlers is that the HTML structure of the press and featured page differ slightly. When first wrtiting this program, it was assumed that both pages shared the same HTML structure and cause bugs when tryig to scrape the image URL. Keep this in mind if more sites are added to the program.

### Running the program

Scrapy applications can be run from the command line, so that's how we will do it:

1. Open a terminal and navigate to the base directory of this project (i.e .../lwr-news-scraper/)
2. Type this command into the terminal:  
```
      scrapy crawl lwr_spider
  ```
3. Press Enter, and you should see something similar to this (this is just the first part, there is a lot more that is not pasted here):

```
        $ scrapy crawl lwr_spider
        2020-05-29 13:24:16 [scrapy.utils.log] INFO: Scrapy 2.1.0 started (bot: lwr_news_scraper)
        2020-05-29 13:24:16 [scrapy.utils.log] INFO: Versions: lxml 4.5.1.0, libxml2 2.9.5, cssselect 1.1.0, parsel 1.6.0, w3lib 1.22.0, Twisted 20.3.0, Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)], pyOpenSSL 19.1.0 (OpenSSL 1.1.1g  21 Apr 2020), cryptography 2.9.2, Platform Windows-10-10.0.18362-SP0
        2020-05-29 13:24:16 [scrapy.utils.log] DEBUG: Using reactor: twisted.internet.selectreactor.SelectReactor
        2020-05-29 13:24:16 [scrapy.crawler] INFO: Overridden settings:
        {'BOT_NAME': 'lwr_news_scraper',
         'NEWSPIDER_MODULE': 'lwr_news_scraper.spiders',
         'ROBOTSTXT_OBEY': True,
         'SPIDER_MODULES': ['lwr_news_scraper.spiders']}
        2020-05-29 13:24:16 [scrapy.extensions.telnet] INFO: Telnet Password: b9b5a54906395f5e
        2020-05-29 13:24:16 [py.warnings] WARNING: c:\users\oscar\appdata\local\programs\python\python37\lib\site-packages\scrapy\extensions\feedexport.py:210: ScrapyDeprecationWarning: The `FEED_URI` and `FEED_FORMAT` settings have been deprecated in favor of the `FEEDS` setting. Please see the `FEEDS` setting docs for more details
          exporter = cls(crawler)


```

4. If no error messages appear in the output, there should now be a __.JSON__ file present in the base directory of the project titled,
__articles.json__. As the name suggests, this file holds article objects in JSON format containing four fields: Title, content, link (url), and image url.
