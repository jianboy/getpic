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
from crawl_image.libs.download_progress import DownloadProgress
from concurrent.futures import ThreadPoolExecutor
from contextlib import closing
from crawl_image import api
import requests
import json
import re
import os
import sys


class CrawlImageFromSogou(CrawlImage):
    def __init__(self):
        super().__init__()
        self.imageList = []
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
        preInt = self.max_download_images // pageSize
        afterInt = self.max_download_images % pageSize
        if afterInt == 0:
            preInt = preInt
        else:
            preInt = preInt+1
        for page in range(preInt):
            url = api.sogou_getImage % (page*pageSize, self.keyword)
            try:
                response = self.session.get(url)
                self.imageList.extend(json.loads(
                    response.text)['data']["items"])
            except Exception as e:
                print(e)
                continue

    def downloadPic(self, picUrl: str, fileName: str):
        '''
        download a picture
        '''
        with closing(self.sess.get(url=picUrl, stream=True, timeout=10)) as response:
            chunkSize = 1024
            contentSize = int(response.headers["content-length"])
            if(os.path.exists(fileName) and os.path.getsize(fileName) == contentSize):
                print("跳过" + fileName)
            else:
                progress = DownloadProgress(fileName, total=contentSize, unit="KB",
                                            chunk_size=chunkSize, run_status="downloading", fin_status="downloaded")
                if not os.path.exists(os.path.dirname(fileName)):
                    os.makedirs(os.path.dirname(fileName))
                with open(fileName, "wb") as file:
                    for data in response.iter_content(chunk_size=chunkSize):
                        file.write(data)
                        progress.refresh(count=len(data))

    def run(self):
        self.getImageList()

        # download pictures
        with ThreadPoolExecutor(max_workers=10) as executor:
            for image in self.imageList[:self.max_download_images]:
                fileName = self.savedir +"sogou_{}_{}".format(self.keyword, str(image['index']+1)) + ".jpg" # + image['picUrl'].split('.')[-1]
                executor.submit(self.downloadPic, image['picUrl'], fileName)
