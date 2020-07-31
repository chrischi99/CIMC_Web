# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import numpy as np
import pandas as pd
import tkinter as tk
from pandas import DataFrame
from tkinter import filedialog
from tkinter import messagebox
from tkinter import simpledialog

class NewsCrawlerPipeline:
    global title_list 
    title_list = []
    def open_spider(self, spider):
        self.fo = open('搜索结果.csv', 'a')
        title = "{},{},{},{},{}\n".format("标题", "发布时间","URL","新闻机构","简介")
        self.fo.write(title)

    def process_item(self, item, spider):
        global title_list
        if (item['title'] not in title_list):
            data = "{},{},{},{},{}\n".format(item['title'],item['publish_time'],item['url'],item['media_name'],item['description'])
            self.fo.write(data)
            title_list.append(item['title'])
        return item

    def close_spider(self, spider):
        self.fo.close()
