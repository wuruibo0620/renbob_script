# -*- coding: utf-8 -*-
from time import sleep
from urllib.error import URLError
import re

import scrapy
from LJ.items import LjName


class LjNameSpider(scrapy.Spider):
    name = 'lj_name'
    allowed_domains = ['rossia.org']
    start_urls = ['http://lj.rossia.org/users/vrotmnen0gi/']
    head_url = 'http://lj.rossia.org/users/vrotmnen0gi/?skip='
    page = 0

    def parse(self, response):
        if self.page < 374:
            url_page = self.head_url + str((self.page + 1) * 20)
            while True:
                try:
                    yield scrapy.Request(url=url_page, callback=self.parse)
                    print(f'当前第{self.page}页{url_page}')
                    break
                except URLError as e:
                    print(e)
                    sleep(1)

        girls = response.xpath('//table/tr/td/table')
        for girl in girls:
            item_name = LjName()
            flag = girl.xpath('./tr/td[@class="caption"]/text()').extract_first()
            if flag and not re.match('( Pussy Por| disclaimer)', flag):
                item_name['name'], = re.findall('^ ?(.*)$', flag)
                item_name['img_url'] = girl.xpath('./tr/td//a/img/@src').extract_first()
                item_name['link_url'] = girl.xpath('./tr/td[@class="comments"][1]/a/@href').extract_first()
                item_name['page'] = str(self.page)

                yield item_name
        sleep(0.2)
        self.page += 1
