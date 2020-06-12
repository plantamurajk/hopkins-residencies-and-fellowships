import scrapy
import ndjson
import re
import string

import pdb


import logging

from datetime import datetime, date

from ..items import ResidentOrFellowItem

URLS = ["https://www.jhsph.edu/academics/residency-programs/general-preventive-medicine-residency/who-we-are/current-residents.html"]

class PreventiveRadiologyResidents(scrapy.Spider):
    name = 'preventive_medicine_residents'
    start_urls  = URLS

    def parse(self, response):

        items = ResidentOrFellowItem()

        residents = response.xpath("//div[@class='wrapper']")

        for res in residents:
            items['current_year'] = res.xpath("ancestor::div/preceding-sibling::h2/text()").getall()[-1]
            items['name'] = res.xpath("h3//text()").get()
            items['image_url'] = response.urljoin(res.xpath("descendant-or-self::img/@src").get())
        # items['name'] = response.xpath("//div[@class='image-list-image']/img/@src").getall()
            items['program_type'] = 'Residency'
            items['specialty'] = 'General Preventive Medicine'
        # response.xpath("//div[@class='image-list-image']/ancestor-or-self::div/preceding-sibling::h2/text()").getall()
            yield items

        