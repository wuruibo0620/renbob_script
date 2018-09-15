# -*- coding: utf-8 -*-
import re

from text_spider.items import TextSpiderItem
import scrapy
from time import sleep


class ZolSpider(scrapy.Spider):
    name = 'ZOL'
    allowed_domains = ['detail.zol.com.cn']
    start_urls = ['http://detail.zol.com.cn/digital_camera_index/subcate15_0_list_1_0_1_2_0_1.html',]
                  # 'http://detail.zol.com.cn/digital_camera_index/subcate15_0_list_1_0_1_2_0_2.html',
                  # 'http://detail.zol.com.cn/digital_camera_index/subcate15_0_list_1_0_1_2_0_3.html',
                  # 'http://detail.zol.com.cn/digital_camera_index/subcate15_0_list_1_0_1_2_0_4.html',
                  # 'http://detail.zol.com.cn/digital_camera_index/subcate15_0_list_1_0_1_2_0_5.html']

    page_url = 'http://detail.zol.com.cn/digital_camera_index/subcate15_0_list_1_0_1_2_0_'
    page = 1
    def parse(self, response):
        cameras = response.xpath("//div[@class='wrapper clearfix']/div[@class='content']/div[@class='pic-mode-box']/ul[@id='J_PicMode']/li")
        for camera in cameras:
            item = TextSpiderItem()
            item['name'] = camera.xpath("./h3/a/@title").extract_first()
            item['price'] = camera.xpath("./div[@class='price-row']/span/b[@class='price-type']/text()").extract_first()
            flag = re.findall(r'(万)',item['price'])
            if flag :
                n = re.findall(r'\d+\.?\d*',item['price'])
                item['price'] = str(float(n[0]) * 10000)

            item['score'] = camera.xpath("./div[@class='comment-row']/span[@class='score']/text()").extract_first()
            item['num_plp'] = camera.xpath("./div[@class='comment-row']/a[@class='comment-num']/text()").extract_first()
            item['num_plp'] = re.match(r'(\d*)',item['num_plp'])[0]
            item['img_url'] = camera.xpath("./a/img/@*[3]").extract_first()    # xpath匹配
            # item['img_url'] = camera.re('<a href.*src="(https://.*\.[a-z]*)".*</a>')[0]   # 正则匹配
            print(item['num_plp'])


            next_url = camera.xpath("./a[@class='pic']/@href").extract_first()
            next_url = 'http://detail.zol.com.cn/'+next_url
            sleep(0.1)
            yield scrapy.Request(url=next_url, callback=self.parse_next, meta={"item": item})


    def parse_next(self,response):
        item = response.meta["item"]
        item['title'] = response.xpath("//div[@class='product-model page-title clearfix']/h1[@class='product-model__name']/text()").extract_first()
        item['price_ref'] = response.xpath("//div[@class='product-price-box clearfix ']/div[@class='price__reference']/div/span/b[2]/text()").extract_first()
        item['price_shop'] = response.xpath("//div[@class='price__other']/dl[@class='price__merchant']/dd[@id='_j_local_price']/a[@class='price']/text()").extract_first()
        item['shop'] = response.xpath("//div[@class='product-price-box clearfix ']/div[@class='price__other']/dl[@class='price__b2c']/dd//li/a/text()").extract_first()
        item['parameter'] = response.xpath("//div[@class='content']/div[@class='section'][1]/div[@class='section-content']/ul[@class='product-param-item pi-15 clearfix']/li/p/text()").extract_first()

        yield item

