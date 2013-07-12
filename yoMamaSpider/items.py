from scrapy.item import Item, Field


class JokeItem(Item):
    joke = Field()
    tags = Field()
