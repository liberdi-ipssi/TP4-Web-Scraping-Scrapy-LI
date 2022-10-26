from datetime import datetime
import scrapy
from scrapy import Request
from WebCrawler.items import ReviewsBoursoramaItem
from WebCrawler.pipelines import WebcrawlerPipeline

class BoursoramaSpider(scrapy.Spider):
    pipeline = WebcrawlerPipeline()
    name = 'boursorama'
    allowed_domains = ['finance.yahoo.com']
    start_urls = [f'https://www.boursorama.com/bourse/actions/palmares/france/page-{n}?france_filter%5Bmarket%5D=1rPCAC' for n in range(1,3)]

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse_boursorama)
            
    def parse_boursorama(self, response):
        liste_indices = response.css('tr.c-table__row')[1:]
        
        for indices in liste_indices:
            item = ReviewsBoursoramaItem()
            
            #indice boursier
            try: 
              item['indice'] = indices.css('td.c-table__cell.c-table__cell--dotted.u-text-uppercase').css('a::text').get()
            except:
              item['indice'] = 'None'
            
            #indice cours de l'action
            try: 
              item['cours'] = indices.css('span.c-instrument.c-instrument--last::text').get()
            except:item['cours'] = 'None'
            
            #Variation de l'action
            try: 
              item['var'] = indices.css('span.c-instrument.c-instrument--instant-variation::text').get()
            except:
              item['var'] = 'None'
            
            #Valeur la plus haute
            try: 
              item['hight'] = indices.css('span.c-instrument.c-instrument--high::text').get()
            except:
              item['hight'] = 'None'
            
            #Valeur la plus basse
            try: 
              item['low'] = indices.css('span.c-instrument.c-instrument--low::text').get()
            except:
              item['low'] = 'None'

            #Valeur d'ouverture
            try: 
              item['open_'] = indices.css('span.c-instrument.c-instrument--open::text').get()
            except:
              item['open_'] = 'None'

            #Date de la collecte
            try: 
              item['time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            except:
              item['time'] = 'None'

            self.pipeline.process_item_boursorama(item)

            yield item