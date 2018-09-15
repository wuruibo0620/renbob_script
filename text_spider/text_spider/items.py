# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TextSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    price = scrapy.Field()
    score = scrapy.Field()
    num_plp = scrapy.Field()
    img_url = scrapy.Field()

    title = scrapy.Field()
    price_ref = scrapy.Field()
    price_shop = scrapy.Field()
    shop = scrapy.Field()
    parameter = scrapy.Field()



