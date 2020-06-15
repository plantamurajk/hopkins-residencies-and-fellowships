# # -*- coding: utf-8 -*-
# import scrapy
# import ndjson
# import re
# import string
# import pdb
# import logging
# from datetime import datetime, date
# from ..items import ResidentOrFellowItem

# URLS = ['PUT THE URL HERE']


# class GENERICResidentsOrFellowsSpider(scrapy.Spider):
#     name = 'GENERIC_residents/fellows'
#     start_urls = URLS


#     def parse(self, response):
#         items = ResidentOrFellowItem()

        
#         residents = response.xpath("div")

#         for res in residents:
#             items['current_year'] = res.xpath('preceding-sibling::h2/text()').getall()[-1]
#             items['grad_year'] = (datetime.today().year + 4) - int(res.xpath('preceding-sibling::h2/text()').getall()[-1][-1])
#             items['name'] = res.xpath("descendant-or-self::h4/text()").get()
#             items['image_url'] = response.urljoin(res.xpath("descendant-or-self::img/@src").get())
#             items['program_type'] = ''
#             items['specialty'] = ''
#             yield items
