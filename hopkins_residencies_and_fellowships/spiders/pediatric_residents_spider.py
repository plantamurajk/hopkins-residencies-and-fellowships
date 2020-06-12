import scrapy
import ndjson
import re
import string

import pdb


import logging

from datetime import datetime, date

from ..items import ResidentOrFellowItem

URLS = ["https://www.hopkinsmedicine.org/johns-hopkins-childrens-center/healthcare-professionals/education/residency-program/current-residents.html"]

class PediatricsResidentSpider(scrapy.Spider):
    name = 'pediatrics_residents'
    start_urls  = URLS

    def parse(self, response):

        items = ResidentOrFellowItem()

        tables = response.xpath('//table[@class="overflow_alt_rows"]')
        for table in tables:
            rows = table.xpath('tr')
            for row in rows:
                cols = row.xpath('td//text()').extract()
                if not cols:
                    continue
                name = cols[0]
                medical_school = cols[1]
                items['name'] = name
                items['program_type'] = 'Residency'
                items['specialty'] = 'Pediatrics'

                # if (len(cols) == 2):
                #     years = table.xpath("../preceding-sibling::h4//text()").getall()
                #     if years: 
                #         items['year'] = years[-1]
                # elif(len(cols) == 3):
                #     items['year'] = cols[2]
                yield items

        