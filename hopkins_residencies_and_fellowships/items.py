# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ResidentOrFellowItem(scrapy.Item):
    source_url = scrapy.Field()
    name = scrapy.Field()
    specialty = scrapy.Field()
    program_type = scrapy.Field()
    grad_year = scrapy.Field()
    current_year = scrapy.Field()
    program = scrapy.Field()
    
