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

        # parallel arrays of articles and content
        articleList = response.css(ARTICLE_SELECTOR)
        contentList = response.css(CONTENT_SELECTOR)

        # Iterate through every article found
        for articleIndx in range(len(articleList)):

            # CSS extension for title in each article
            TITLE_SELECTOR = 'a ::text'
            DESCRIPTION_SELECTOR = 'p ::text'
            
            yield {
                # Title field will be the first instance of TITLE_SELECTOR in each article
                'title': articleList[articleIndx].css(TITLE_SELECTOR).extract_first(),
                'content': contentList[articleIndx].css(DESCRIPTION_SELECTOR).extract_first(),
                
            }

        

    
