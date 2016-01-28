#!/usr/bin/python
#-*-coding:utf-8-*-

#from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.http import Request
from baicaio.items import *
from baicaio.utils import *
import json


class baicaioSpider(CrawlSpider):
    name = "baicaio"
    allowed_domains=["baicaio.com"]
    start_urls = ["http://www.baicaio.com"]
    counters = 0
    #categories_lx = LinkExtractor(restrict_xpaths='//ul[@class="post-list"]')
    #details_lx=LinkExtractor(restrict_xpaths='//ul[@class="post-list"]')
    #rules = (
    #    Rule(categories_lx)
     #       )


    def parse(self, response):
        response_selector = Selector(response)
        next_link = list_first_item(response_selector.xpath(\
            u'//div[@class="pagenav"]/a[text()="下一页"]/@href').extract())
        if next_link:
            print("next_link:"+ next_link)
            yield Request(url=next_link, callback=self.parse)

        details_links = response_selector.xpath(\
            u'//ul[@class="post-list"]/li/h2/a/@href').extract()
        for details_link in details_links:
            if details_link:
                print("details_link:"+ details_link)
                yield Request(url=details_link, callback=self.parse_detail)

    def parse_detail(self, response):
        bc_item = baicaioItem()
        response_selector = Selector(response)
        bc_item['g_title'] = list_first_item(response_selector.xpath(\
            '//ul/li/h1/a/@title').extract())
        print("title %s" % (list_first_item(response_selector.xpath(\
            '//ul/li/h1/a/@title').extract())))
        self.counters += 1
        bc_item['g_id'] = self.counters
        bc_item['g_description'] = list_first_item(response_selector.xpath(\
            '//ul/li/div[@class="content"]/p').extract()).encode('utf-8')
       # bc_item['g_date'] = list_first_item(response_selector.xpath(u'//div[@class="date"]/text()').extract()) + " " + \
       #     + list_first_item(response_selector.xpath(u'//div[@class="time"]/text()').extract())
        bc_item['g_type'] = list_first_item(response_selector.xpath('//div[@class="cats"]/a/text()').extract())


        #bc_item['g_brand'] = list_first_item(response_selector.xpath().extract())

        return bc_item

