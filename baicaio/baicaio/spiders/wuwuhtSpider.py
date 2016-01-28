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
    name = "wwht"
    allowed_domains=["55haitao.com"]
    start_urls = ["http://www.55haitao.com/deals"]
    counters = 0
    #categories_lx = LinkExtractor(restrict_xpaths='//ul[@class="post-list"]')
    #details_lx=LinkExtractor(restrict_xpaths='//ul[@class="post-list"]')
    #rules = (
    #    Rule(categories_lx)
     #       )

    g_query = { 'g_title' : '//div[@class="ht-deal-detail-title clearfix"]/h1/a/text()',
        'g_description' : '//div[@class="inner-block"]/p[@itemprop="description"]',
        'g_catalog' : '//div[@class="article_meta"][2]/span[2]/a[2]/text()',
        'g_brand' : '//div[@class="article_meta"][3]/span[@class="brands"]/a/text()',
        'g_tags' : '//p[@class="ht-deal-detail-info-tag]"/a/text()',
        'g_date' : '//div[@class="article_meta"][1]/span[not(@class)]/text()'}

    def parse(self, response):
        response_selector = Selector(response)

        next_link = list_first_item(response_selector.xpath(\
            '//a[@class="pager-next"]/@href').extract())
        if next_link:
            print("next_link:"+ next_link)
            yield Request(url=next_link, callback=self.parse)

        details_links = response_selector.xpath(\
            '//h1[@class="index-deal-title"]/a/@href').extract()
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

        g_tags = response_selector.xpath(self.g_query['g_tags']).xpath('string(.)').extract()
        bc_item['g_tags'] = g_tags
        bc_item['g_brand'] = response_selector.xpath(self.g_query['g_brand']).extract()

        bc_item['g_date'] = list_first_item(response_selector.xpath(self.g_query['g_date']).extract())
        #bc_item['g_time'] = list_first_item(response_selector.xpath(\
        #    '//div[@class="time"]/text()').extract())
        bc_item['g_update_time'] = datetime.datetime.utcnow()
        #dianci='点此前往'.decode('gb2312')
        #print('dianci'+dianci)
        #g_source_str = list_first_item(response_selector.xpath("//a/text()[contains(.,dianci)]"))
        #g_source = g_source_str.replace('点此前往','').replace('购买地址','')
        #print('source1 %s source2 %s' %(g_source_str, g_source))
        #bc_item['g_source'] = g_source

        return bc_item

