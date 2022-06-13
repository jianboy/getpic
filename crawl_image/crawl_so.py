#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Contact :   liuyuqi.gov@msn.cn
@Time    :   2022/06/13 10:09:01
@License :   Copyright © 2017-2022 liuyuqi. All Rights Reserved.
@Desc    :   
'''
from crawl_image.crawl_image import CrawlImage
from crawl_image.libs.download_progress import DownloadProgress
from concurrent.futures import ThreadPoolExecutor
import requests
import json
import re
import os
import sys


class CrawlImageFromSo(CrawlImage):
    def __init__(self):
        super().__init__()
        pass

    def getImageList(slef):
        pass

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
