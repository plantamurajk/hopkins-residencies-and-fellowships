# -*- coding: utf-8 -*-
import scrapy
import ndjson
import re
import string
import pdb
import logging
from datetime import datetime, date
from ..items import ResidentOrFellowItem

URLS = ['https://www.hopkinsmedicine.org/neurology_neurosurgery/education/residencies/neurosurgery_residency/current_residents/']


class NeurosurgeryResidentsSpider(scrapy.Spider):
    name = 'neurosurgery_residents'
    allowed_domains = ['https://www.hopkinsmedicine.org/neurology_neurosurgery/education/residencies/neurosurgery_residency/current_residents/']
    start_urls = URLS

    def parse(self, response):
        items = ResidentOrFellowItem()

        
        residents = response.xpath('//div[@class="listIndividualWrapper"]')

        for res in residents:
            items['current_year'] = res.xpath('ancestor-or-self::*/preceding-sibling::h2/text()').getall()[-1]
            # items['grad_year'] = (datetime.today().year + 4) - int(res.xpath('preceding-sibling::h2/text()').getall()[-1][-1])
            items['name'] = res.xpath('descendant-or-self::h4/text()').get()
            items['image_url'] = response.urljoin(res.xpath("descendant-or-self::img/@src").get())
            items['program_type'] = 'Residency'
            items['specialty'] = 'Neurosurgery'
            yield items



