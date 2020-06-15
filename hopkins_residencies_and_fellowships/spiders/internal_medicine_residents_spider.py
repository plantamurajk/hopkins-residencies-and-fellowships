# -*- coding: utf-8 -*-
import scrapy
import ndjson
import re
import string

import pdb

import logging
from datetime import datetime, date

from ..items import ResidentOrFellowItem

URLS = ['https://www.hopkinsmedicine.org/Medicine/education/internal_medicine_residency_program/current-residents.html']

class InternalMedicineResidentsSpider(scrapy.Spider):
    name = 'internal_medicine_residents'
    allowed_domains = ['https://www.hopkinsmedicine.org/Medicine/education/internal_medicine_residency_program/current-residents.html']
    start_urls = URLS

    def parse(self, response):
        items = ResidentOrFellowItem()

        residents = response.xpath('//h3')

        for res in residents:
            items['name'] = res.xpath('text()').get()
            items['current_year'] = res.xpath('preceding-sibling::h2/a/attribute::name').getall()[-1]
            items['image_url'] = response.urljoin(res.xpath('preceding-sibling::div/img/attribute::src').getall()[-1])
            items['program_type'] = 'Residency'
            items['specialty'] = 'Internal Medicine'
            yield items