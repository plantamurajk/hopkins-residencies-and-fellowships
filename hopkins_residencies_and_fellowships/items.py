# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HopkinsResidentOrFellow(scrapy.Item):
    name = scrapy.Field()
    grad_year = scrapy.Field()
    specialty = scrapy.Field()
    program_type = scrapy.Field()
    pass
