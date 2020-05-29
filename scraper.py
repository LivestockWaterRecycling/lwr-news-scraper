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
        SET_SELECTOR = '.uk-panel-title'

        #Iterate through every article found
        for brickset in response.css(SET_SELECTOR):
            TITLE_SELECTOR = 'a ::text'

            #A lot of fast facts - excluding them for now... 
            if not 'FAST FACTS' in str(brickset.css(NAME_SELECTOR).extract_first()) :   
                yield {
                    #Title field will be the first instance of TITLE_SELECTOR in each article
                    'title': brickset.css(TITLE_SELECTOR).extract_first(),
                }

        

    
