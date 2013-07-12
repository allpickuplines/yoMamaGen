# Scrapy settings for yoMamaSpider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'yoMamaSpider'

SPIDER_MODULES = ['yoMamaSpider.spiders']
NEWSPIDER_MODULE = 'yoMamaSpider.spiders'

ITEM_PIPELINES = [
        'yoMamaGen.pipelines.YomamaspiderPipeline',
    ]

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'yoMamaSpider (+http://www.yourdomain.com)'
