# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import time
import urllib
import os
from time import sleep


class retry:
    def __init__(self, max_times=3, sleep_time=0, exceptions=(Exception,)):
        self.max_times = max_times
        self.sleep_time = sleep_time
        self.exceptions = exceptions

    def __call__(self, func):
        def wrap(a, item, spider):
            for count in range(self.max_times):
                try:
                    result = func(a, item, spider)
                except self.exceptions:
                    sleep(self.sleep_time)
                else:
                    return result
        return wrap


class LjPipeline(object):
    count = 1297

    def process_item(self, item, spider):
        self.count += 1
        flag = item['name']
        list_dir = os.listdir('H:\\try\\')
        if flag not in list_dir:
            os.makedirs("H:\\try\\" + flag)
        str1 = str(int(time.time()))
        file_name = "H:\\try\\" + flag + '\\' + str1 + ".jpg"
        for _ in range(3):
            try:
                img_data = urllib.request.urlopen(url=item['img_url'], timeout=12).read()
                with open(file_name, 'wb') as f:
                    f.write(img_data)
                # urllib.request.urlretrieve(url=item['img_url'], filename=file_name)
                print("爬取到的图片数量:%d张,请去文件夹查看!" % self.count)
                break
            except Exception as e:
                print(e, '下载')
                sleep(0.5)


class LjNamePiple(object):
    def open_spider(self, spider):
        self.LJ = open('LJ.json', 'w', encoding='utf-8', )
        self.items = []

    def process_item(self, item, spider):
        detail = {
            'name' : item['name'],
            'img_url' : item['img_url'],
            'link_url' : item['link_url'],
            'page' : item['page']
        }
        self.items.append(detail)

    def close_spider(self, spider):
        self.LJ.write(json.dumps(self.items, ensure_ascii=False) + "\n")
        self.LJ.close()

