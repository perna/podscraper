# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import requests


class AllPodcastsPipeline(object):

    def __init(self):
        self.send_to_api()

    def process_item(self, item, spider):
        self.send_to_api(item)
        return item

    def send_to_api(self,item):
        data = {"name": item["name"], "feed": item["feed"]}
        header = {'Content-type': 'application/json'}
        post = requests.post("https://podigger.xyz/api/podcasts/", data=json.dumps(data), headers=header)
