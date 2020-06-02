###
# This program uses scrapy to 'crawl' or 'spider' through the news/featured page of the LWR Website.
#
# Author: Oscar Jaimes
# Date: 29/05/2020
###

import scrapy

class LWRSpider(scrapy.Spider):
    
    name = "lwr_spider_featured"

    # urls that this spider crawls through. Crawls through 1 URL at a time.
    start_urls = ['https://www.livestockwaterrecycling.com/newsroom/featured.html' ]
        

    ###
    # Function that parses a websites HTML source
    # @param response - HTML response
    ###
    def parse(self, response):
        # extension for different sections of a given article
        ARTICLE_SELECTOR = '.uk-panel-title'
        CONTENT_SELECTOR = '.uk-margin'
        IMAGE_SELECTOR = '.uk-overlay.uk-overlay-hover '

        # parallel arrays of article components
        titleList = response.css(ARTICLE_SELECTOR)
        contentList = response.css(CONTENT_SELECTOR)
        imageList = response.css(IMAGE_SELECTOR)

        
        # Iterate through every article found
        for articleIndx in range(len(titleList)):

            # Extensions for each field:
            # CSS:
            TITLE_EXTENSION = 'a ::text'
            DESCRIPTION_EXTENSION = 'p ::text'
            # xPath
            LINK_EXTENSION = 'a/@href'
            IMAGE_EXTENSION = 'img/@src'
            
            # Will append to end of this string when constructing image link.
            IMAGE_URL_START = 'https://www.livestockwaterrecycling.com/'

            # resulting dictionary/map of each article object
            yield {
                'title': titleList[articleIndx].css(TITLE_EXTENSION).extract_first(),
                'content': contentList[articleIndx].css(DESCRIPTION_EXTENSION).extract_first(),
                'link': titleList[articleIndx].xpath(LINK_EXTENSION).extract_first(),
                'image': IMAGE_URL_START + imageList[articleIndx].xpath(IMAGE_EXTENSION).extract_first(),
            }

        

    
