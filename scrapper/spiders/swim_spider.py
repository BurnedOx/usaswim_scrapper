import scrapy
from scrapy_selenium import SeleniumRequest


class SwimSpiderSpider(scrapy.Spider):
    name = 'swim_spider'
    
    def start_requests(self):
        yield SeleniumRequest( 
            url ="http://https://www.usaswimming.org/times/popular-resources/event-rank-search/", 
            wait_time = 3, 
            screenshot = True, 
            callback = self.parse,  
            dont_filter = True    
        )

    def parse(self, response):
        pass
