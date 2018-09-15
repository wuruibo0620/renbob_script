# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import csv
import json

import pymysql


class TextSpiderPipeline(object):
    def open_spider(self, spider):
        self.cameraFile_json = open("index.json", "w", encoding="utf-8")
        self.cameraItems_json = []

        self.movieFile_csv = open("list.csv", "w", encoding="utf-8")
        self.movieItems_csv = []
        print("开始处理数据...")

    def process_item(self, item, spider):
        print("=====================================================================")
        print(item)
        dic = dict(item)
        self.cameraItems_json.append(dic)

        csv_item = []
        csv_item.append(item["name"])
        csv_item.append(item["price"])
        csv_item.append(item["score"])
        csv_item.append(item["num_plp"])
        csv_item.append(item["img_url"])
        self.movieItems_csv.append(csv_item)

        return item

    def close_spider(self, spider):
        # print(self.movieItems)
        self.cameraFile_json.write(json.dumps(self.cameraItems_json,ensure_ascii=False))
        self.cameraFile_json.close()

        writor = csv.writer(self.movieFile_csv)
        writor.writerow(["name", "price", "score", "num_plp", "img_url"])
        writor.writerows(self.movieItems_csv)
        print("数据处理结束！")



class MysqlPipeline(object):
    def __init__(self):
        self.host = "127.0.0.1"
        self.port = 3306
        self.user = 'root'
        self.passwoerd = 'ruibo3359404'
        self.dbname = 'spider'
        pass

    def open_spider(self, spider):
        self.conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.passwoerd,
            db=self.dbname,
            charset='utf8'
        )
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        # print("=======================================")
        sql = "INSERT INTO camera VALUES (NULL,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (item["name"], item["price"], item["score"], item["num_plp"], item["img_url"],item["title"], item["price_ref"], item["price_shop"], item["shop"], item["parameter"])
        self.cursor.execute(sql)
        self.conn.commit()

        return item

    def close_spider(self, spider):
        self.conn.close()
        self.cursor.close()