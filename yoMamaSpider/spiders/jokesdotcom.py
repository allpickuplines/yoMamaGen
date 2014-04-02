from scrapy.contrib.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.http import Request
from yoMamaSpider.items import JokeItem
from yoMamaSpider.striputils import stripcats, stripjokes
import re

class JokesDotComSpider(CrawlSpider):
    name = 'jokesdotcom'
    allowed_domains = ['jokes.com']
    start_urls = ["http://www.jokes.com/funny-yo--mama"]

    def parse(self, response):
        hxs = Selector(response)
        links = hxs.xpath('//a')
        for link in links:
            url = ''.join(link.xpath('./@href').extract())
            relevant_urls = re.compile(
                'http://www\.jokes\.com/funny-yo--mama/([a-zA-Z0-9]+)/yo-([a-zA-Z]+)')
            if relevant_urls.match(url):
                print url
    #             yield Request(url, callback=self.parse_page)

    # def parse_page(self, response):
    #     hxs = Selector(response)
    #     categories = stripcats(hxs.select('//title/text()').extract())
    #     joke_area = hxs.select('//p/text()').extract()
    #     for joke in joke_area:
    #         joke = stripjokes(joke)
    #         if len(joke) > 15:
    #             yield JokeItem(joke=joke, categories=categories)
