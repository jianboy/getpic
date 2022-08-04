#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Contact :   liuyuqi.gov@msn.cn
@Time    :   2022/06/13 10:09:01
@License :   Copyright © 2017-2022 liuyuqi. All Rights Reserved.
@Desc    :   
'''
from concurrent.futures import ThreadPoolExecutor
from getpic.crawl_image import CrawlImage
from getpic import api
import json


class CrawlImageFromSogou(CrawlImage):

    def __init__(self):
        super().__init__()
        self.imageList = []
        self.setBigImage()

    def setBigImage(self):
        self.sess.get(api.sogou_host)
        response = self.sess.get(api.sogou_setBigImage)
        return response.content

    def getImageList(self):
        pageSize = 48
        preInt = self.max_download_images // pageSize
        afterInt = self.max_download_images % pageSize
        if afterInt == 0:
            preInt = preInt
        else:
            preInt = preInt + 1
        for page in range(preInt):
            url = api.sogou_getImage % (page*pageSize, self.keyword)
            try:
                response = self.sess.get(url)
                self.imageList.extend(json.loads(
                    response.text)['data']["items"])
            except Exception as e:
                print(e)
                continue

    def run(self):
        self.getImageList()

        # download pictures
        with ThreadPoolExecutor(max_workers=10) as executor:
            for image in self.imageList[:self.max_download_images]:
                # + image['picUrl'].split('.')[-1]
                fileName = self.savedir + \
                    "sogou_{}_{}".format(
                        self.keyword, str(image['index']+1)) + ".jpg"
                executor.submit(self.downloadPic, image['picUrl'], fileName)
