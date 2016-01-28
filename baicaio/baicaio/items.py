# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class baicaioItem(scrapy.Item):
<<<<<<< HEAD
    _id = scrapy.Field()
=======
>>>>>>> fbe35a3351ed5f4a29b308fed48b89aa1d0c0c46
    g_id = scrapy.Field()
    g_description = scrapy.Field()
    g_title = scrapy.Field()
    g_brand = scrapy.Field()
<<<<<<< HEAD
    g_tags = scrapy.Field()
    g_date = scrapy.Field()
    g_time = scrapy.Field()
    g_price_rmb = scrapy.Field()
    g_price_my = scrapy.Field()
    g_price_origin = scrapy.Field()
    g_details = scrapy.Field()
    g_source = scrapy.Field()
    g_catalog = scrapy.Field()
    g_rate = scrapy.Field()
    g_link = scrapy.Field()
    g_mongoid = scrapy.Field()
    g_update_time = scrapy.Field()
=======
    g_price_C = scrapy.Field()
    g_price_D = scrapy.Field()
    g_price_O = scrapy.Field()
    g_date = scrapy.Field()
    g_details = scrapy.Field()
    g_source = scrapy.Field()
    g_type = scrapy.Field()
    g_rate = scrapy.Field()
    g_size = scrapy.Field()
    g_originalLink = scrapy.Field()
    g_mongoid = scrapy.Field()
>>>>>>> fbe35a3351ed5f4a29b308fed48b89aa1d0c0c46
