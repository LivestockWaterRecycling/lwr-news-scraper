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
    start_urls = ['https://www.livestockwaterrecycling.com/newsroom/press.html']

    ###
    # Function that parses a websites HTML source
    # @param response - HTML response
    ###
    def parse(self, response):
        # extension for each 'news article' in HTML source
        ARTICLE_SELECTOR = '.uk-panel-title'
        CONTENT_SELECTOR = '.uk-margin'
        

        # parallel arrays of article components
        titleList = response.css(ARTICLE_SELECTOR)
        contentList = response.css(CONTENT_SELECTOR)

        # Iterate through every article found
        for articleIndx in range(len(titleList)):

            # CSS extension for title in each article
            TITLE_SELECTOR = 'a ::text'
            DESCRIPTION_SELECTOR = 'p ::text'
            LINK_SELECTOR = 'href ::text'
            
            yield {
                'title': titleList[articleIndx].css(TITLE_SELECTOR).extract_first(),
                'content': contentList[articleIndx].css(DESCRIPTION_SELECTOR).extract_first(),
                'link': titleList[articleIndx].xpath('a/@href').extract_first(),
            }

        

    
