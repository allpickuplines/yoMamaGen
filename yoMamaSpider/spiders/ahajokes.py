from scrapy.contrib.spiders import CrawlSpider
from scrapy.selector import HtmlXPathSelector
from yoMamaSpider.items import JokeItem
from yoMamaSpider.striptags import strip_tags
import urlparse
import re


class AhaJokesSpider(CrawlSpider):
    name = 'ahajokes'
    allowed_domains = ['ahajokes.com']
    start_urls = []
    for x in xrange(3):
        for y in xrange(9):
            start_urls.append("http://www.ahajokes.com/ym"
                              + x + y + ".html")

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        m = re.search(r'ym\d{2}-(\d+)\.html', response.url)
        page = m.groups()[0]
        next_page = int(page) + 1

        url = urlparse.urljoin(response.url, 'ym01-%s.html' % next_page)
        self.log(url)
        yield Request(url, callback=self.parse)

        tag = strip_tags(hxs.select('//title').extract())

        for joke_box in hxs.select('//div[@id="Joke_box"]').extract():
            for joke in joke_box.split("<br><br>"):
                joke = re.sub(r'<br>', ' ', joke).trim()
                yield JokeItem(joke=joke.strip(), tags=tag)
