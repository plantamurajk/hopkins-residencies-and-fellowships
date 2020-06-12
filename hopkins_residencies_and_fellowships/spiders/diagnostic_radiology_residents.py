import scrapy
import ndjson
import re
import string

import pdb


import logging

from datetime import datetime, date

from ..items import ResidentOrFellowItem

URLS = ["https://www.hopkinsmedicine.org/radiology/education/residency/diagnostic-radiology-residency-program/meet-our-residents.html"]
class DiagnosticRadiologyResidents(scrapy.Spider):
    name = 'diagnostic_radiology_residents'
    start_urls  = URLS

    def parse(self, response):

        items = ResidentOrFellowItem()

        residents = response.xpath("//div[starts-with(@class,'image-list-item')]")

        for res in residents:
            items['current_year'] = res.xpath("ancestor-or-self::div/preceding-sibling::h2/text()").getall()[-1]
            items['name'] = " ".join(res.xpath("descendant-or-self::h3/text()").get().split())
            #
            ## CHECK THIS BELOW
            items['image_url'] = res.xpath("descendant-or-self::img/@src").get()
        # items['name'] = response.xpath("//div[@class='image-list-image']/img/@src").getall()
            items['program_type'] = 'Residency'
            items['specialty'] = 'Diagnostic Radiology'
        # response.xpath("//div[@class='image-list-image']/ancestor-or-self::div/preceding-sibling::h2/text()").getall()
            yield items

        