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



class CrawlImageFromSo(CrawlImage):
    def __init__(self):
        super().__init__()
        self.imageList= []

    def getImageList(self):
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
