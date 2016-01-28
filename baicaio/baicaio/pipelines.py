# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class BaicaioPipeline(object):
    def process_item(self, item, spider):
<<<<<<< HEAD
=======

>>>>>>> fbe35a3351ed5f4a29b308fed48b89aa1d0c0c46
        return item
