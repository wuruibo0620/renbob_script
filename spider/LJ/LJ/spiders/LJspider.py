# -*- coding: utf-8 -*-
from time import sleep

import scrapy
import re

from LJ.items import LjItem


class retry:
    def __init__(self, max_times=3, sleep_time=0, exceptions=(Exception,)):
        self.max_times = max_times
        self.sleep_time = sleep_time
        self.exceptions = exceptions

    def __call__(self, func):
        def wrap(*args, **kwargs):
            for count in range(self.max_times):
                try:
                    result = func(*args, **kwargs)
                except self.exceptions:
                    sleep(self.sleep_time)
                else:
                    return result

        return wrap


class LjspiderSpider(scrapy.Spider):
    name = 'LJspider'
    allowed_domains = ['rossia.org', 'imagenpic.com']
    # start_urls = ['http://lj.rossia.org/users/vrotmnen0gi/']
    start_urls = ['http://lj.rossia.org/users/vrotmnen0gi/?skip=1640']

    head_url = 'http://lj.rossia.org/users/vrotmnen0gi/?skip='    # 翻页时固定不变的url地址
    page = 0   # 起始页为第0页

    def parse(self, response):
        target_list = ['Cali', 'Zelda', 'Jeff Milton']
        'Jeff Milton'
        girl_list = response.xpath("//table/tr/td/table")
        for girl in girl_list:
            name = girl.xpath("./tr[1]/td[@class='caption']/text()").extract_first()
            if name:
                name, = re.findall(r'^\s(.*)', name)
            if name not in target_list:
                continue
            item = LjItem()
            item['name'] = name
            next_url = girl.xpath("./tr[3]/td[2]/a/@href").extract_first()
            # print(next_url)
            sleep(0.2)
            yield scrapy.Request(url=next_url, callback=self.parse_next, meta={'item': item})

        # 翻到下一页
        self.page += 1
        if self.page < 376:    # 设定翻页的页数
            url_page = self.head_url + str(self.page * 20)
            print(url_page)
            print('===================================================================1111')
            while True:
                try:
                    yield scrapy.Request(url=url_page, callback=self.parse)
                    break
                except Exception as e:
                    print(e, '请求')
                    sleep(0.1)

    def parse_next(self, response):    # 请求二级页面
        item = response.meta['item']
        img_str = response.text
        reg = re.compile(r'style="TEXT-ALIGN: center">.*mment</a></td>', re.S)
        img_str1 = re.findall(reg, img_str)[0]
        reg1 = re.compile(r'>(<a href="https?://.*?\.jpg"><img border="0" src="http://.*?\.jpg"></a>)<br />&nbsp;')
        img_list = re.findall(reg1, img_str1)
        print(len(img_list))
        for i in img_list:
            item['img_url'] = re.findall(r'<a href="(https?://.*?\.jpg)">', i)[0]
            if re.search(r'imagenpic', item['img_url']):
                item['img_url'] = re.findall(r'<img border="0" src="(http://.*?\.jpg)"></a>', i)[0]
            #     sleep(0.2)
                # yield scrapy.Request(url=i, callback=self.parse_second, meta={'item': item})
                # continue
            # print('===================================================================2222')
            print(item['img_url'])
            yield item

    # def parse_second(self, response):
    #     item = response.meta['item']
    #     item['img_url'] = response.xpath("//p/img/@src").extract_first()
    #     print('===================================================================3333')
    #     print(item['img_url'])
    #     yield item
