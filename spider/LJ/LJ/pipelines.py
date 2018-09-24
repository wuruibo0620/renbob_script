# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import urllib
import os

class LjPipeline(object):
    # count = 1
    # # flag = ''
    # def process_item(self, item, spider):
    #     self.count += 1
    #     # flag = item['name']
    #     file_name = "H:\\try\\" + str(self.count) + ".jpg"
    #     # if self.flag != item['name']:
    #     #     self.flag = item['name']
    #     #     self.count -= 1
    #     urllib.request.urlretrieve(url=item['img_url'], filename=file_name)
    #     print("爬取到的图片数量:%d张,请去文件夹查看!" % self.count)


    n = 0
    def process_item(self, item, spider):
        filename = r"H:\try\\" + str(self.n) + ".jpg"
        urllib.request.urlretrieve(url=item["img_url"], filename=filename)
        self.n += 1
        print("爬取到的图片数量:%d张,请去文件夹查看!" % self.n)
