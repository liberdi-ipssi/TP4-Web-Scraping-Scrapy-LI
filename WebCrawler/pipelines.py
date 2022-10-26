# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sys
sys.path.insert(0, 'C:/Users/lahou/Documents/IPSSI/WebScraping/')

from utiles import DataBase
import sqlalchemy as db

class WebcrawlerPipeline:
    bdd = DataBase('database')
    bdd.create_table('allocine', title=db.String(255), img=db.String(1000), author=db.String(255), time=db.String(255), genre=db.String(255), score=db.String(255), desc=db.String(20000), release=db.String(255))
    
    def process_item_allocine(self, item):
        self.bdd.add_row('allocine', title=str(item['title']), img=str(item['img']), author=str(item['author']), time=str(item['time']), genre=str(item['genre']), score=str(item['score']), desc=str(item['desc']), release=str(item['release']))
        return item
