#!/usr/bin/python
#-*-coding:utf-8-*-

#from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.http import Request
from baicaio.items import *
from baicaio.utils import *
import datetime
#import json


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

    g_query = { 'g_title' : '//*[@id="content"]/ul/li/h1/a/@title',\
    	'g_description' : '//*[@id="content"]/ul/li/div[@class="content"]' ,\
        'g_catalog' : '//*[@id="content"]/ul/li/div[@class="cats"]/a/text()',}

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
            self.g_query['g_title']).extract())

        self.counters += 1
        bc_item['g_id'] = self.counters
        str = list_first_item(response_selector.xpath(\
            self.g_query['g_description']))
        g_description = ''.join(list_first_item(str.xpath('string(.)').extract()).split())
        bc_item['g_description'] = g_description

        bc_item['g_catalog'] = list_first_item(response_selector.xpath(\
            self.g_query['g_catalog']).extract())
        bc_item['g_link'] = response.url

        g_tags = response_selector.xpath('//div[@class="tags"]/a').xpath('string(.)').extract()
        bc_item['g_tags'] = g_tags
        bc_item['g_brand'] = list_first_item(g_tags)

        bc_item['g_date'] = list_first_item(response_selector.xpath(\
            '//div[@class="date"]/text()').extract())
        bc_item['g_time'] = list_first_item(response_selector.xpath(\
            '//div[@class="time"]/text()').extract())
        bc_item['g_update_time'] = datetime.datetime.utcnow()
        #dianci='点此前往'.decode('gb2312')
        #print('dianci'+dianci)
        #g_source_str = list_first_item(response_selector.xpath("//a/text()[contains(.,dianci)]"))
        #g_source = g_source_str.replace('点此前往','').replace('购买地址','')
        #print('source1 %s source2 %s' %(g_source_str, g_source))
        #bc_item['g_source'] = g_source

        return bc_item

