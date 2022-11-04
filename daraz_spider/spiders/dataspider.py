import scrapy


class DataspiderSpider(scrapy.Spider):
    name = 'dataspider'
    allowed_domains = ['daraz.com']
    start_urls = ['http://daraz.com/']

    def parse(self, response):
        pass
