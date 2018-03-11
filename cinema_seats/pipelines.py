# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem

class CinemaSeatsPipeline(object):
    def process_item(self, item, spider):
        return item

class DuplicatesPipeline(object):

    def __init__(self):
        self.cinema_set = set()

    def process_item(self, item, spider):
        cinema_info = item['cinema_name'] + item['room_num']
        if cinema_info in self.cinema_set:
            raise DropItem('Duplicate book found:%s' % item)
        self.cinema_set.add(cinema_info)
        return item