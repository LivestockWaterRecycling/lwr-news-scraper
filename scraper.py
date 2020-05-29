###
# This program uses scrapy to 'crawl' or 'spider' through the news page of the LWR Website.
#
# Author: Oscar Jaimes
# Date: 29/05/2020
###

import scrapy

class LWRSpider(scrapy.Spider):
    name = "lwr_spider"
    start_urls = ['https://www.livestockwaterrecycling.com/newsroom/featured.html']

    ###
    # Function that parses a websites HTML source
    # @param response - HTML response
    ###
    def parse(self, response):
        #extension for each 'news article' in HTML source
        ARTICLE_SELECTOR = '.uk-panel-title'

        #Iterate through every article found
        for article in response.css(ARTICLE_SELECTOR):
            TITLE_SELECTOR = 'a ::text'

            #A lot of fast facts - excluding them for now... TODO
            if not 'FAST FACTS' in str(brickset.css(NAME_SELECTOR).extract_first()) :   
                yield {
                    #Title field will be the first instance of TITLE_SELECTOR in each article
                    'title': article.css(TITLE_SELECTOR).extract_first(),
                }

        

    
