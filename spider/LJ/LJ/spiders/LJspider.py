# -*- coding: utf-8 -*-
from time import sleep

import scrapy
import re

from LJ.items import LjItem


class LjspiderSpider(scrapy.Spider):
    name = 'LJspider'
    allowed_domains = ['rossia.org']
    start_urls = ['http://lj.rossia.org/users/vrotmnen0gi/']
    head_url = 'http://lj.rossia.org/users/vrotmnen0gi/?skip='    # 翻页时固定不变的url地址
    page = 0    # 起始页为第0页

    def parse(self, response):
        target_list = ['Lizzie',]
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
        if self.page < 1:    # 设定翻页的页数
            url_page = self.head_url + str(self.page * 20)
            print(url_page)
            print('====================================================++++++++++++++++++')
            yield scrapy.Request(url=url_page, callback=self.parse)

    @staticmethod
    def parse_next(response):    # 请求二级页面
        item = response.meta['item']
        img_str = response.text
        reg = re.compile(r'style="TEXT-ALIGN: center">.*mment</a></td>', re.S)
        img_str1 = re.findall(reg, img_str)[0]
        print(img_str1)
        reg1 = re.compile(r'><a (href="http://.*\.jpg)"><img border="0" src="http://.*\.jpg"></a><br />&nbsp;')
        img_list = re.findall(reg1, img_str1)
        for i in img_list:
            print("===============================================================")
            print(i)


















        # img_list = response.xpath("//table[@class='entrybox']//table//div[@style='TEXT-ALIGN: center']//a/@href").extract()
        # img_list = response.xpath("//table[@class='entrybox']//table//div[@style='TEXT-ALIGN: center']//a")
        # for img_url in img_list:
        #     item['img_url'] = img_url.xpath("./@href").extract_first()
        #     flag = re.match(r'http://jpegshare', item['img_url'])
        #     if not flag:
        #         item['img_url'] = img_url.xpath('./@src').extract_first()
        #     print(item['img_url'])
        #
        #
        #
        # for img_url in img_list:
        #     item['img_url'] = img_url
        #     print(img_url)
        #     yield item
