# -*- coding: utf-8 -*-

# Scrapy settings for cinema_seats project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random
BOT_NAME = 'cinema_seats'
SPIDER_MODULES = ['cinema_seats.spiders']
NEWSPIDER_MODULE = 'cinema_seats.spiders'
FEED_EXPORT_FIELDS = ['cinema_name', 'room_num', 'all_num']
ROBOTSTXT_OBEY = False
DEFAULT_REQUEST_HEADERS = {
    'DNT': 1,
    'Accept-Encoding': "gzip, deflate",
    'Accept-Language': "zh-CN,zh;q=0.9",
    'Upgrade-Insecure-Requests': "1",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'Cache-Control': "no-cache",
    'Cookie': "_lxsdk=161658cf0cdc8-0de22982ba06fc-3c604504-e1000-161658cf0cd80; uuid=1A6E888B4A4B29B16FBA1299108DBE9CEA6C7AFFDEFBF75A8235B02C850AA34F; _lx_utm=utm_source%3Dbaidu%26utm_medium%3Dorganic; _csrf=f25a28e378b1ddc3698f259656964e65c83aba80df56e2c6e2950a5f94895d8b; __mta=214153768.1517827207525.1517881319737.1517881413851.47; _lxsdk_s=cdbd58d2a6156068c4179155a0f1%7C%7C24",
    'Connection': "keep-alive",
}
DOWNLOAD_DELAY = random.random()
ITEM_PIPELINES = {
    'cinema_seats.pipelines.CinemaSeatsPipeline': 300,
    'cinema_seats.pipelines.DuplicatesPipeline': 350,
}

#USER_AGENT_LIST = [
#    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7',
#    'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0) Gecko/16.0 Firefox/16.0',
#    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10',
#    ]

#HTTP_PROXY = 'http://127.0.0.1:8123'

#DOWNLOADER_MIDDLEWARES = {
#    'cinema_seats.middlewares.RandomUserAgentMiddleware': 400, # 修改这里的myspider为项目名称
#    'cinema_seats.middlewares.ProxyMiddleware': 410, # 同上
#    'cinema_seats.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
#}
# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'cinema_seats.middlewares.CinemaSeatsSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'cinema_seats.middlewares.CinemaSeatsDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
