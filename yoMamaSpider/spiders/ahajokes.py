from scrapy.contrib.spiders import CrawlSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request, FormRequest
from yoMamaSpider.items import JokeItem
from yoMamaSpider.striptags import striptags
import urlparse
import re


class AhaJokesSpider(CrawlSpider):
    name = 'ahajokes'
    allowed_domains = ['ahajokes.com']
    start_urls = []
    for x in xrange(3):
        for y in xrange(9):
            start_urls.append("http://www.ahajokes.com/ym"
                              + str(x) + str(y) + ".html")
            start_urls.append("http://www.ahajokes.com/ym"
                              + str(x) + str(y) + "-1.html")

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        m = re.search(r'ym\d{2}-(\d+)\.html', response.url)
        if m:
            page = m.groups()[0]
            next_page = int(page) + 1
            url = urlparse.urljoin(response.url, str(response.url)[0:str(response.url).find('-')] + '-%s.html' % next_page)
        else:
            url = response.url

        self.log(url)
        yield Request(url, callback=self.parse)

        categories = striptags(hxs.select('//title/text()').extract())

        for joke_box in hxs.select('//div[@id="Joke_box"]/text()').extract():
            for joke in joke_box.split("<br><br>"):
                joke = joke[0:joke.find('i Submitted by')].strip()
                if joke != '':
                    yield JokeItem(joke=joke, categories=categories)
