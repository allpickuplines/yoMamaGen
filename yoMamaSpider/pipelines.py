from scrapy import log
from pysqlite2 import dbapi2 as sqlite


class YomamaspiderPipeline(object):
    def __init__(self):
        # Possible we should be doing this in spider_open instead, but okay
        self.connection = sqlite.connect('../../yomama.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS joke ' \
                            '(id INTEGER PRIMARY KEY, joke TEXT NOT NULL, categories TEXT NOT NULL)')

    def process_item(self, item, spider):
        self.cursor.execute("select * from joke where joke=?", item['joke'])
        result = self.cursor.fetchone()
        if result:
            log.msg("Item already in database: %s" % item, level=log.DEBUG)
        else:
            self.cursor.execute(
                "insert into joke (joke, categories) values (?, ?)",
                    (item['joke'][0], item['categories'][0])

            self.connection.commit()

            log.msg("Item stored : " % item, level=log.DEBUG)
        return item

    def handle_error(self, e):
        log.err(e)
