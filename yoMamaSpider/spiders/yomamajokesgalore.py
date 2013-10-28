from scrapy.contrib.spiders import CrawlSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from yoMamaSpider.items import JokeItem
from yoMamaSpider.striputils import stripcats, stripjokes
import re

class YoMamaJokesGalore(CrawlSpider):
    name = 'yomamajokesgalore'
    allowed_domains = ['yomamajokesgalore.com']
    start_urls = ['http://www.yomamajokesgalore.com/']

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        links = hxs.select('//a')
        urls = []
        for link in links:
            url = ''.join(link.select('./@href').extract())
            irrelevant_urls = re.compile(
                '(index\.html|links\.html|contact\.html|http(s?)://.*)')
            if not irrelevant_urls.match(url) and url not in urls:
                urls.append(url)
                url = "http://www.yomamajokesgalore.com/" + url
                yield Request(url, callback=self.parse_page)

    def parse_page(self, response):
        hxs = HtmlXPathSelector(response)
        categories = stripcats(hxs.select('//title/text()').extract())
        joke_area = hxs.select('//table[contains(@width, "500")]/tr/td//text()').extract()
        for joke in joke_area:
            joke = stripjokes(joke)
            if len(joke) > 15:
                yield JokeItem(joke=joke, categories=categories)
