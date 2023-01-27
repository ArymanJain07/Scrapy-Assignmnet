import scrapy
from ..items import AmazonItem

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = [

        'https://www.amazon.in/s?k=books&ref=pd_sl_551nkgifm8_b'

    ]

    def parse(self, response):
        items = AmazonItem()

        product_name = response.css('.a-size-medium::text').extract()
        product_author = response.css('.a-color-secondary .a-size-base+ .a-size-base , .a-color-secondary .a-size-base.s-link-style').css('::text').extract()
        product_prize = response.css('.a-price-whole::text').extract()
        product_imageLink = response.css('.s-image::attr(src)').extract()

        items['product_name'] = product_name
        items['product_author'] = product_author
        items['product_prize'] = product_prize
        items['product_imageLink'] = product_imageLink

        yield items
