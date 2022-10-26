# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sys
sys.path.insert(0, '../../utiles.py')

from utiles import DataBase
import sqlalchemy as db

class WebcrawlerPipeline:
    bdd = DataBase('database')
    
    bdd.create_table('allocine', title=db.String(255), img=db.String(1000), author=db.String(255), time=db.String(255), genre=db.String(255), score=db.String(255), desc=db.String(20000), release=db.String(255))
    bdd.create_table('boursorama', indice=db.String(255), cours=db.String(255), var=db.String(255), hight=db.String(255), low=db.String(255), open_=db.String(255), time=db.String(255))

    def process_item_allocine(self, item):
        self.bdd.add_row('allocine', title=str(item['title']), img=str(item['img']), author=str(item['author']), time=str(item['time']), genre=str(item['genre']), score=str(item['score']), desc=str(item['desc']), release=str(item['release']))
        return item

    def process_item_boursorama(self, item):
        self.bdd.add_row('boursorama', indice=str(item['indice']), cours=str(item['cours']), var=str(item['var']), hight=str(item['hight']), low=str(item['low']), open_=str(item['open_']), time=str(item['time']))
        return item
