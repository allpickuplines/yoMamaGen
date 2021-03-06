from scrapy.contrib.spiders import CrawlSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from yoMamaSpider.items import JokeItem
from yoMamaSpider.striputils import stripcats, stripjokes
import re

class Jokes4UsSpider(CrawlSpider):
    name = 'jokes4us'
    allowed_domains = ['jokes4us.com']
    start_urls = ["http://www.jokes4us.com/yomamajokes/"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        links = hxs.select('//a')
        for link in links:
            url = ''.join(link.select('./@href').extract())
            relevant_urls = re.compile(
                'http://www\.jokes4us\.com/yomamajokes/yomamas([a-zA-Z]+)')
            if relevant_urls.match(url):
                yield Request(url, callback=self.parse_page)

    def parse_page(self, response):
        hxs = HtmlXPathSelector(response)
        categories = stripcats(hxs.select('//title/text()').extract())
        joke_area = hxs.select('//p/text()').extract()
        for joke in joke_area:
            joke = stripjokes(joke)
            if len(joke) > 15:
                yield JokeItem(joke=joke, categories=categories)
