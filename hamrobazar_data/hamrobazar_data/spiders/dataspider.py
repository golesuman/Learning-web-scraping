import scrapy
import json
import datetime as dt
from scrapy_playwright.page import PageMethod
class DataspiderSpider(scrapy.Spider):
    name = 'dataspider'
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Access-Control-Allow-Origin': '*',
        'ApiKey': '09BECB8F84BCB7A1796AB12B98C1FB9E',
        'DeviceId': '3ef647d1-9d66-43bd-ae3c-80a87a260264',
        'DeviceSource': 'web',
        'Referer': 'https://hamrobazaar.com/',
        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'Strict-Transport-Security': 'max-age=2592000',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        'X-Content-Type-Options':'nosniff',
        'X-Frame-Options': 'SAMEORIGIN',
    }
    def start_requests(self):
        page_no = 1
        while page_no != 100:
            url = f'https://api.hamrobazaar.com/api/Product?PageSize=100&CategoryId=&IsHBSelect=false&PageNumber={page_no}' 
            page_no += 1
            yield scrapy.Request(url=url, headers=self.headers)


    def parse(self, response, **kwargs):
        data = response.body.decode('utf-8')
        json_data = json.loads(data)
        

        # data_json = ''.join(json_date)
        previous_date = dt.datetime.today() - dt.timedelta(days=7)
        
        # print(f'date of 3 days before {previous_date}')
        # print(f'Json date is {new_json_date}')
        i = 0
        while i<100:
            creation_date = json_data['data'][i]['createdOn']
            new_json_date = " ".join(creation_date.split("T"))
            formatted_date = new_json_date.split(".")[0]
            previous_date = str(previous_date).split(".")[0]
            if  dt.datetime.strptime(previous_date, "%Y-%m-%d %H:%M:%S") < dt.datetime.strptime(formatted_date,"%Y-%m-%d %H:%M:%S"):
                name = json_data['data'][i]['name']
                description = json_data['data'][i]['description']
                creator = json_data['data'][i]['creatorInfo']['createdByName']
                price = json_data['data'][i]['price']
                image_url = json_data['data'][i]['imageUrl']
                location = json_data['data'][i]['location']['locationDescription']
                category = json_data['data'][i]['categoryName']
                i += 1
                # print(name)
                yield{
                    'name' : name,
                    'created_on' : formatted_date, 
                    'description' : description,
                    'created_by' : creator,
                    'price' : price,
                    'image_url' : image_url,
                    'location' : location,
                    'category' : category,
                    
                    # ''
                    
                }
            
            else:
                break
