#encoding:utf-8
#!/usr/bin/python
#-*-coding:utf-8-*-

"""
"""

import types
from pymongo import MongoClient
import jieba

DATABASE_NAME = "baicaio"
client = None
DATABASE_HOST = "localhost"
DATABASE_PORT = 27017
INDEX = {\
            #collection
            'g_detail':{'g_id':1}\
        }

def drop_database(name_or_database):
    if name_or_database and client:
        client.drop_database(name_or_database)

def printItem(collection):
    counter = 0
    for item in collection.find():
        seg_list = jieba.cut(item['g_description'],cut_all=False)
        print(','.join(seg_list))
        counter += 1
        if counter > 10:
            break

def collect_tags(collection):
    brand_counter = 0
    d_tags = dict()
    for item in collection.find():

        item_tags = item['g_brand']
        if item_tags in d_tags.keys():
            d_tags[item_tags] += 1
        else:
            d_tags[item_tags] = 0
    print sorted(d_tags.items(), key=lambda d: d[1])
    for (k,v) in d_tags.items():
        brand_counter+=1
    print("counter: %d" % brand_counter)


def create_index():
    """
        create index for baicaio_fs.g_details
    """
    for k,v in INDEX.items():
        for key,kwargs in v.items():
            client[DATABASE_NAME][k].ensure_index(list(key) if type(key)==types.TupleType else key,**kwargs)

if __name__ == "__main__":
    client = MongoClient(DATABASE_HOST,DATABASE_PORT)
    bc_db = client.baicaio
    bc_collection = bc_db.zdm_details
    collect_tags(bc_collection)

#    drop_database(DATABASE_NAME)
#    create_index()
