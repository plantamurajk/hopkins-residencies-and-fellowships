import scrapy
import ndjson
import re
import string

import pdb


import logging

from datetime import datetime, date

from ..items import ResidentOrFellowItem

URLS = ["https://www.hopkinsmedicine.org/emergencymedicine/em-residency/people/pgy1.html",
"https://www.hopkinsmedicine.org/emergencymedicine/em-residency/people/pgy2.html",
"https://www.hopkinsmedicine.org/emergencymedicine/em-residency/people/pgy3.html",
"https://www.hopkinsmedicine.org/emergencymedicine/em-residency/people/pgy4.html"]
class EmergencyMedicineResidents(scrapy.Spider):
    name = 'emergency_medicine_residents'
    start_urls  = URLS

    def parse(self, response):

        items = ResidentOrFellowItem()

        
        residents = response.xpath("//div[@class='listIndividualWrapper']")

        for res in residents:
            items['current_year'] = response.xpath('//h1[@class="mainBodyContentTitle"]//text()').get()
            items['grad_year'] = 2020 + (4 - int(response.url[-6]))
            items['name'] = res.xpath("h2/text()").get()
            items['image_url'] = response.urljoin(res.xpath('div/img/@src').get())
            items['program_type'] = 'Residency'
            items['specialty'] = 'Emergency Medicine'
            yield items

        