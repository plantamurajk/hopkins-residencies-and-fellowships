# -*- coding: utf-8 -*-
import scrapy
import ndjson
import re
import string
import pdb
import logging
from datetime import datetime, date
from ..items import ResidentOrFellowItem

URLS = ["https://www.hopkinsmedicine.org/brady-urology-institute/education/residency/residents.html"]




class UrologyResidentsSpider(scrapy.Spider):
    name = 'urology_residents'
    # allowed_domains = ['https://www.hopkinsmedicine.org/brady-urology-institute/education/residency/residents.html']
    start_urls = URLS

    def parse(self, response):
        items = ResidentOrFellowItem()

        
        residents = response.xpath('//div[@class="listIndividualWrapper"]')

        for res in residents:
            items['current_year'] = res.xpath('preceding-sibling::h2//text()').getall()[-1]
            # items['grad_year'] = (datetime.today().year + 4) - int(res.xpath('preceding-sibling::h2/text()').getall()[-1][-1])
            items['name'] = res.xpath('preceding-sibling::h3//text()').getall()[-1]
            items['image_url'] = response.urljoin(res.xpath('descendant-or-self::img//attribute::src').get())
            items['program_type'] = 'Residency'
            items['specialty'] = 'Urology'
            yield items

