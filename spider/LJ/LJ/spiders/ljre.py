# -*- coding: utf-8 -*-
from time import sleep

import scrapy
import re

from LJ.items import LjItem


class LjreSpider(scrapy.Spider):
    name = 'ljre'
    allowed_domains = ['rossia.org', 'imagenpic.com']
    # start_urls = ['http://lj.rossia.org/users/vrotmnen0gi/']
    start_urls = ['http://lj.rossia.org/users/vrotmnen0gi/?skip=4720']    # 3520开始有没有下完的，3840 报错
    # start_urls = ['http://lj.rossia.org/users/vrotmnen0gi/?skip=3720']
    # start_urls = ['http://lj.rossia.org/users/vrotmnen0gi/?skip=4400']
    # start_urls = ['http://lj.rossia.org/users/vrotmnen0gi/?skip=5360']
    head_url = 'http://lj.rossia.org/users/vrotmnen0gi/?skip='    # 翻页时固定不变的url地址
    page = 236   # 起始页为第0页

    def parse(self, response):
        target_list = ['Cali', 'Zelda', 'Maria', 'Kaleesy', 'Clarice']
        target_list = [ 'Sade Mare', 'Gloria Sol']
        target_str = '(' + '|'.join(target_list) + ')'
        # print(target_str) Cali|Olya R|Milena|Faina Bona
        # reg_1 = re.compile(r'<td class="caption"> Raisa</td>.*?<a href="http://lj\.rossia\.org/users/vrotmnen0gi/\d+\.html\?mode=reply">Leave a comment</a>', re.S)
        reg_1 = re.compile(r'(<td class="caption"> (Dominika|Stefani|Sofie|Sati|Sabrina)</td>.*?<a href="http://lj\.rossia\.org/users/vrotmnen0gi/\d+\.html\?mode=reply">Leave a comment</a>)', re.S)
        girls_str = response.text
        girl_list = re.findall(reg_1, girls_str)
        # print(girl_list)
        for girl1 in girl_list:
            # print(girl1)
            girl = girl1[0]
            name, = re.findall(r'<td class="caption"> (.*?)</td>.*?<a href="http://lj\.rossia\.org/users/vrotmnen0gi/\d+\.html\?mode=reply">Leave a comment</a>', girl, re.S)
            print(name)
            item = LjItem()
            item['name'] = name
            next_url, = re.findall(r'<a href="(http://lj\.rossia\.org/users/vrotmnen0gi/\d+\.html\?mode=reply)">Leave a comment</a>', girl, re.S)
            print(next_url)
            sleep(0.05)
            yield scrapy.Request(url=next_url, callback=self.parse_next, meta={'item': item})

        # 翻到下一页
        self.page += 1
        if self.page < 375:    # 设定翻页的页数(最大380）
            url_page = self.head_url + str(self.page * 20)
            print(f'当前第{self.page}页')
            print(url_page)

            # print('===================================================================1111')
            while True:
                try:
                    yield scrapy.Request(url=url_page, callback=self.parse)
                    break
                except Exception as e:
                    print(e, '请求')
                    sleep(0.05)

    def parse_next(self, response):    # 请求二级页面
        item = response.meta['item']
        img_str = response.text
        reg = re.compile(r'style="TEXT-ALIGN: center">.*comment</a></td>', re.S)
        img_str1 = re.findall(reg, img_str)[0]
        reg1 = re.compile(r'>(<a ?href="https?://.*?\.(html|jpg)(.html)?".*?><img ?(border="0")? ?src="https?://.*?\.jpg" ?(border="0")?></a>) ?<br')
        img_list = re.findall(reg1, img_str1)
        # print(img_list)
        print(len(img_list))
        for i in img_list:
            # print(i[0])
            if re.search(r'<a href="https?://.*?\.jpg"', i[0]):
                item['img_url'], = re.findall(r'<a href="(https?://.*?\.jpg)"', i[0])
            else:
                item['img_url'] = ''
            if re.search(r'(imagenpic|img\.yt/|imgbar|imageshimage|radikal)', item['img_url']):
                # item['img_url'], = re.findall(r'<img ?border="0" src="(https?://.*?\.jpg)"></a>', i[0])
                item['img_url'], = re.findall(r'<img.*?src="(https?://.*?\.jpg)".*?></a>', i[0])
            print(item['img_url'])
            yield item
