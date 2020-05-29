###
# This program uses scrapy to 'crawl' or 'spider' through the news page of the LWR Website.
# It will crawl two specific pages in the LWR website - newsroom/press and newsroom/featured
#
# Author: Oscar Jaimes
# Date: 29/05/2020
###

import scrapy

class LWRSpider(scrapy.Spider):
    name = "lwr_spider"

    # urls that this spider crawls through. Crawls through 1 URL at a time.
    start_urls = ['https://www.livestockwaterrecycling.com/newsroom/press.html',
                  'https://www.livestockwaterrecycling.com/newsroom/featured.html' ]

    ###
    # Function that parses a websites HTML source
    # @param response - HTML response
    ###
    def parse(self, response):
        # extension for each 'news article' in HTML source
        ARTICLE_SELECTOR = '.uk-panel-title'
        CONTENT_SELECTOR = '.uk-margin'
        IMAGE_SELECTOR = '.uk-overlay.uk-overlay-hover '

        

        # parallel arrays of article components
        titleList = response.css(ARTICLE_SELECTOR)
        contentList = response.css(CONTENT_SELECTOR)
        imageList = response.css(IMAGE_SELECTOR)

        print("\n\n\n" + str(len(imageList)) + "\n\n\n")
        print(imageList)

        # Iterate through every article found
        for articleIndx in range(len(titleList)):

            # CSS extension for title in each article
            TITLE_SELECTOR = 'a ::text'
            DESCRIPTION_SELECTOR = 'p ::text'
            LINK_SELECTOR = 'a/@href'
            IMAGE_EXTENSION = 'img/@src'

            IMAGE_URL_START = 'https://www.livestockwaterrecycling.com/'

            
            yield {
                'title': titleList[articleIndx].css(TITLE_SELECTOR).extract_first(),
                'content': contentList[articleIndx].css(DESCRIPTION_SELECTOR).extract_first(),
                'link': titleList[articleIndx].xpath(LINK_SELECTOR).extract_first(),
                'image': IMAGE_URL_START + imageList[articleIndx].xpath(IMAGE_EXTENSION).extract_first(),
            }

        

    
