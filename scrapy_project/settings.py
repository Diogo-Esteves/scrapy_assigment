# -*- coding: utf-8 -*-

# Scrapy settings for assignment project
#
BOT_NAME = 'scrapy_project'

SPIDER_MODULES = ['scrapy_project.spiders']
NEWSPIDER_MODULE = 'scrapy_project.spiders'

LOG_LEVEL = 'WARNING'

HTTPERROR_ALLOWED_CODES  = [404]

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'assignment (+http://www.yourdomain.com)'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 50

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
