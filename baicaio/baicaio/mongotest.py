#!/usr/bin/python
#-*-coding:utf-8-*-

import datetime
import traceback

from scrapy import log
from pymongo.mongo_client import MongoClient

class SingleMongodbPipeline(object):
    """
        save the data to mongodb.
    """

  #  MONGODB_SERVER = "localhost"
  #  MONGODB_PORT = 27017
  #  MONGODB_DB = "baicaio"

    def __init__(self, mongo_server, mongo_port, mongo_table, mongo_collection):
        """
            The only async framework that PyMongo fully supports is Gevent.

            Currently there is no great way to use PyMongo in conjunction with Tornado or Twisted. PyMongo provides built-in connection pooling, so some of the benefits of those frameworks can be achieved just by writing multi-threaded code that shares a MongoClient.
        """
        self.MONGODB_SERVER = mongo_server
        self.MONGODB_PORT = mongo_port
        self.MONGODB_DB = mongo_table
        self.MONGODB_COLLECTION = mongo_collection
        try:
<<<<<<< HEAD
=======
            print("@@@@@@@@@@@@@@@@@@@%s-%s-%s" % (self.MONGODB_SERVER,self.MONGODB_PORT,self.MONGODB_DB))
>>>>>>> fbe35a3351ed5f4a29b308fed48b89aa1d0c0c46
            client = MongoClient(self.MONGODB_SERVER,self.MONGODB_PORT)
            self.db = client[self.MONGODB_DB]
        except Exception as e:
            print("ERROR(SingleMongodbPipeline): %s"%(str(e)))
            traceback.print_exc()

    @classmethod
    def from_settings(cls, settings):
        mongo_server = settings.get('SINGLE_MONGODB_SERVER')
        mongo_port = settings.getint('SINGLE_MONGODB_PORT')
        mongo_table = settings.get('SINGLE_MONGODB_DB')
<<<<<<< HEAD
        mongo_collection = settings.get('SINGLE_MONGODB_COLLECTION')
        return cls(mongo_server, mongo_port, mongo_table, mongo_collection)

    def process_item(self, item, spider):

        result = self.db[self.MONGODB_COLLECTION].insert(item)
        item["g_mongoid"] = str(result)

=======
        mongo_collection = settings.get('SINGLE_ONGODB_COLLECTIONM')
        return cls(mongo_server, mongo_port, mongo_table, mongo_collection)

    def process_item(self, item, spider):
        g_detail = {
            'g_title':item.get('g_title',''),
            'g_description':item.get('g_description',''),
            'g_id':item.get('g_id',''),
            'g_type':item.get('g_type',''),
            'update_time':datetime.datetime.utcnow(),
        }

        result = self.db[self.MONGODB_COLLECTION].insert(g_detail)
        item["g_mongoid"] = str(result)

        print("Item %s wrote to MongoDB database %s/g_details" %
                    (result, g_detail))
>>>>>>> fbe35a3351ed5f4a29b308fed48b89aa1d0c0c46
        return item

class ShardMongodbPipeline(object):
    """
        save the data to shard mongodb.
    """

    MONGODB_SERVER = "localhost"
    MONGODB_PORT = 27017
    MONGODB_DB = "books_mongo"
    GridFs_Collection = "book_file"

    def __init__(self):
        """
            The only async framework that PyMongo fully supports is Gevent.

            Currently there is no great way to use PyMongo in conjunction with Tornado or Twisted. PyMongo provides built-in connection pooling, so some of the benefits of those frameworks can be achieved just by writing multi-threaded code that shares a MongoClient.
        """
        try:
            client = MongoClient(self.MONGODB_SERVER,self.MONGODB_PORT)
            self.db = client[self.MONGODB_DB]
        except Exception as e:
            print("ERROR(ShardMongodbPipeline): %s"%(str(e)))
            traceback.print_exc()

    @classmethod
    def from_crawler(cls, crawler):
        cls.MONGODB_SERVER = crawler.settings.get('ShardMONGODB_SERVER', 'localhost')
        cls.MONGODB_PORT = crawler.settings.getint('ShardMONGODB_PORT', 27017)
        cls.MONGODB_DB = crawler.settings.get('ShardMONGODB_DB', 'books_mongo')
        cls.GridFs_Collection = crawler.settings.get('GridFs_Collection', 'book_file')
        pipe = cls()
        pipe.crawler = crawler
        return pipe

    def process_item(self, item, spider):
        book_detail = {
            'book_name':item.get('book_name'),
            'alias_name':item.get('alias_name',[]),
            'author':item.get('author',[]),
            'book_description':item.get('book_description',''),
            'book_covor_image_path':item.get('book_covor_image_path',''),
            'book_covor_image_url':item.get('book_covor_image_url',''),
            'book_download':item.get('book_download',[]),
            'book_file_url':item.get('book_file_url',''),
            'book_file_id':item.get('book_file_id',''),
            'original_url':item.get('original_url',''),
            'update_time':datetime.datetime.utcnow(),
        }

        result = self.db['book_detail'].insert(book_detail)
        item["mongodb_id"] = str(result)

        log.msg("Item %s wrote to MongoDB database %s/book_detail" %
                    (result, self.MONGODB_DB),
                    level=log.DEBUG, spider=spider)
        return item
