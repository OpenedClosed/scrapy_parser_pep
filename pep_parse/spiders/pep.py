import re

import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        pep_table = response.xpath(
            '//table[@class="pep-zero-table docutils align-default"]/'
            'tbody/tr/td/a[@class="pep reference internal"]/@href'
        )
        for pep_row in pep_table:
            yield response.follow(pep_row, callback=self.parse_pep)

    def parse_pep(self, response):
        pattern = r'^PEP (?P<number>\d+) – (?P<name>.+)$'
        title = response.xpath('//h1[@class="page-title"]/text()').get()
        info_in_title = re.search(pattern, title)
        data = {
            'number': int(info_in_title.group('number')),
            'name': info_in_title.group('name'),
            'status': response.css(
                'dt:contains("Status") + dd abbr::text'
            ).get(),
        }
        print(data)
        yield PepParseItem(data)
