import scrapy

class QuotesScraper(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://quotes.toscrape.com',
    ]

    def parse(self, response, **kwargs):
        quotes_list = response.xpath("//div[@class='quote']//span[@class='text']/text()").getall()
        author_list = response.xpath("//div[@class='quote']//span//small[@class='author']/text()").getall()
        for quote, author in zip(quotes_list, author_list):
            yield {
                'quote' : quote,
                'author' : author,
            }
