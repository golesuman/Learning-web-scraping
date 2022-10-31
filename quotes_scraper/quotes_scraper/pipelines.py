# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3
from itemadapter import ItemAdapter


class QuotesScraperPipeline:
    def __init__(self) -> None:
        self.create_connection()
        self.create_table()
        
         
    def create_connection(self):
        self.conn = sqlite3.connect("myquotes.db")
        self.curr = self.conn.cursor()
    
    def create_table(self):
        self.curr.execute('''drop table if exists quotes_tb''')

        self.curr.execute('''create table quotes_tb (
                             quote text, 
                             author text
                         )''')

    def store_db(self, item):
        query = """insert into quotes_tb ('quote', 'author') values(?, ?)"""
        data = (item['quote'],item["author"])
        self.curr.execute(query, data)
        self.conn.commit()


    def process_item(self, item, spider):
        self.store_db(item)
        # print(f"Pipeline :-  {item['quotes'][0]}")
        return item
