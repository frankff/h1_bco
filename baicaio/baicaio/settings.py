# -*- coding: utf-8 -*-

# Scrapy settings for baicaio project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'baicaio'

SPIDER_MODULES = ['baicaio.spiders']
NEWSPIDER_MODULE = 'baicaio.spiders'

#LOG_FILE = "logs/baicaio.log"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'baicaio (+http://www.yourdomain.com)'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS=32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
<<<<<<< HEAD
#DOWNLOAD_DELAY=3
=======
DOWNLOAD_DELAY=3
>>>>>>> fbe35a3351ed5f4a29b308fed48b89aa1d0c0c46
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN=16
CONCURRENT_REQUESTS_PER_IP=16

# Disable cookies (enabled by default)
COOKIES_ENABLED=False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED=False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'baicaio.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'baicaio.downloadmiddleware.rotate_useragent.RotateUserAgentMiddleware': 300,
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.telnet.TelnetConsole': None,
#}

SINGLE_MONGODB_SERVER = "localhost"
SINGLE_MONGODB_PORT = 27017
SINGLE_MONGODB_DB = "baicaio"
<<<<<<< HEAD
SINGLE_MONGODB_COLLECTION = "zdm_details"
=======
SINGLE_MONGODB_COLLECTION = "bc_details"
>>>>>>> fbe35a3351ed5f4a29b308fed48b89aa1d0c0c46


# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'baicaio.pipelines.BaicaioPipeline': 300,
#   'baicaio.scrapy_redis.pipelines.RedisPipeline': 400,
   'baicaio.mongotest.SingleMongodbPipeline': 350,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# NOTE: AutoThrottle will honour the standard settings for concurrency and delay
<<<<<<< HEAD
AUTOTHROTTLE_ENABLED=False
=======
AUTOTHROTTLE_ENABLED=True
>>>>>>> fbe35a3351ed5f4a29b308fed48b89aa1d0c0c46
# The initial download delay
AUTOTHROTTLE_START_DELAY=5
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY=60
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG=False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED=True
#HTTPCACHE_EXPIRATION_SECS=0
#HTTPCACHE_DIR='httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES=[]
#HTTPCACHE_STORAGE='scrapy.extensions.httpcache.FilesystemCacheStorage'

#SCHEDULER = "baicaio.scrapy_redis.scheduler.Scheduler"
SCHEDULER_PERSIST = False
#SCHEDULER_QUEUE_CLASS = "baicaio.scrapy_redis.queue.SpiderPriorityQueue"


ShardMONGODB_SERVER = "localhost"
ShardMONGODB_PORT = 27017
ShardMONGODB_DB = "baicaio_mongo"
GridFs_Collection = "goods_file"