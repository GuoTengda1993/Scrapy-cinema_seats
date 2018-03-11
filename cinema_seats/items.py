# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class CinemaSeatsItem(scrapy.Item):
    cinema_name = scrapy.Field()
    room_num = scrapy.Field()
    all_num = scrapy.Field()
