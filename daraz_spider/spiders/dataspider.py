import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy_playwright.page import PageMethod
from ..items import DarazSpiderItem
from scrapy.linkextractors import LinkExtractor

class DataspiderSpider(CrawlSpider):
    name = 'dataspider'
    # allowed_domains = ['https://daraz.com/']
    def start_requests(self):
        url = 'https://www.daraz.com.np/'
        yield scrapy.Request(url, meta=dict(
                playwright = True,
                playwright_include_page = True, 
                playwright_page_methods =[
                    PageMethod('wait_for_selector', 'div.box--ujueT')],
            ))
    rules = (
        Rule(LinkExtractor(allow='mens-t-shirts/'), callback='parse_clothes'),
        Rule(LinkExtractor(allow='mens-jackets/')),
        Rule(LinkExtractor(allow='mens-hoodies/')),
        Rule(LinkExtractor(allow='mens-jeans/'))
    )

   
        


    async def parse_clothes(self, response):
        clothes = response.css("div.info--ifj7U")
        print(clothes.get())
        # for cloth in clothes:
        #     title = cloth.css(".title--wFj93 a::attr(href)::text").get()
        #     price = cloth.css("div.price--NVB62::text").get()
        #     yield {
        #         'cloth_name' : title,
        #         'price' : price,
        #     }
        yield
        {
            'clothes' : clothes,
        }

            # print(response.text)


        
