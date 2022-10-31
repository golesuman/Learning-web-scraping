import scrapy
from ..items import QuotesScraperItem

class QuotesScraper(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://quotes.toscrape.com',
    ]

    def parse(self, response, **kwargs):
        items = QuotesScraperItem()
        quotes_list = response.xpath("//div[@class='quote']//span[@class='text']/text()").getall()
        author_list = response.xpath("//div[@class='quote']//span//small[@class='author']/text()").getall()
        for quote, author in zip(quotes_list, author_list):
            items['quotes'] = quote
            items['author'] = author
            yield items

