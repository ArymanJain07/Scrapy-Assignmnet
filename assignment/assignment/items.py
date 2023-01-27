# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonItem(scrapy.Item):
    product_name = scrapy.Field()
    product_author = scrapy.Field()
    product_prize = scrapy.Field()
    product_imageLink = scrapy.Field()

    pass
