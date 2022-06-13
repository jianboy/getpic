#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Contact :   liuyuqi.gov@msn.cn
@Time    :   2022/06/13 10:09:01
@License :   Copyright © 2017-2022 liuyuqi. All Rights Reserved.
@Desc    :   
'''
import imp
from crawl_image.crawl_image import CrawlImage
from crawl_image import api
import requests
import json
import re
import os
import sys


class CrawlImageFromSogou(CrawlImage):
    def __init__(self):
        super().__init__()
        self.session = requests.Session()
        self.session.headers.update(
            {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'})
        self.session.get(api.sogou_host)
        self.setBigImage()

    def setBigImage(self):
        response = self.session.get(api.sogou_setBigImage)
        return response.content

    def getImageList(self):
        pageSize = 48
        imageList=[]
        for page in range(self.max_download_images // pageSize):
            url = api.sogou_getImage % (page*pageSize, self.keyword)
            try:
                response = self.session.get(url)
                imageList.extend(json.loads(response.text)['imgs'])
            except Exception as e:
                print(e)
                continue
        return imageList

    def downloadImage(self, url, filename):
        response = self.session.get(url)
        with open(filename, 'wb') as f:
            f.write(response.content)
        
    def run():
        pass

if __name__ == '__main__':
    CrawlImageFromSogou().getImageList(48)
