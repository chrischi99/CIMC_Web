# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item,Field

class NewsCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    collection = 'news'
    
    publish_time = Field() 
    url = Field()  
    title = Field() 
    media_name = Field()
    description = Field() 
    content = Field()