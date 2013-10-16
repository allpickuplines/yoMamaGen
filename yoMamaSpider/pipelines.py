from scrapy import log
import sqlite3 as sqlite


class YomamaspiderPipeline(object):
    def __init__(self):
        print "Initializing SQLite pipeline."
        # Possible we should be doing this in spider_open instead, but okay
        self.connection = sqlite.connect('../yomama.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS jokes ' \
                            '(id INTEGER PRIMARY KEY, joke TEXT NOT NULL, categories TEXT NOT NULL)')

    def process_item(self, item, spider):
        print "Processing Item"
        joke = (item['joke'],)
        self.cursor.execute("select * from joke where joke=?", joke)
        result = self.cursor.fetchone()
        if result:
            log.msg("Item already in database: %s" % item, level=log.DEBUG)
        else:
            self.cursor.execute("insert into jokes (joke, categories) values (?, ?)",(item['joke'][0], item['categories'][0]))

            self.connection.commit()

            log.msg("Item stored : " % item, level=log.DEBUG)
        return item

    def handle_error(self, e):
        log.err(e)


import json

class JsonWriterPipeline(object):

    def __init__(self):
        self.file = open('items.jl', 'wb')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item
