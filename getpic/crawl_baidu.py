#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Contact :   liuyuqi.gov@msn.cn
@Time    :   2022/06/11 13:42:22
@License :   Copyright © 2017-2022 liuyuqi. All Rights Reserved.
@Desc    :   baidu image search
'''
from concurrent.futures import ThreadPoolExecutor
import re
import os
from getpic.crawl_image import CrawlImage
from getpic import api


class CrawlImageFromBaidu(CrawlImage):
    def __init__(self, keyword="boy", max_download_images=100, savedir=r"data/"):
        super().__init__()

    def run(self):
        url_init = api.baidu_search_image + self.keyword
        allPicUrls = []
        page_urls, next_page_url = self.getPicList(url_init)
        allPicUrls.extend(page_urls)
        os.makedirs(self.savedir, exist_ok=True)
        page_count = 0  # 累计翻页数

    #   获取图片链接
        while True:
            page_urls, next_page_url = self.getPicList(next_page_url)
            page_count += 1
            print('正在获取第%s个翻页的所有图片链接' % str(page_count))
            if next_page_url == '' and page_urls == []:
                print('已到最后一页，共计%s个翻页' % page_count)
                break
            allPicUrls.extend(page_urls)
            if len(allPicUrls) >= self.max_download_images:
                print('已达到设置的最大下载数量%s' % self.max_download_images)
                break

        self.downloadPictures(list(set(allPicUrls)))

    def getPicList(self, pageUrl):
        if not pageUrl:
            return [], ''
        try:
            html = self.sess.get(pageUrl)
            html.encoding = 'utf-8'
            html = html.text
        except IOError as e:
            return [], ''
        pic_urls = re.findall('"objURL":"(.*?)",', html, re.S)
        next_page_url = re.findall(re.compile(r'<a href="(.*)" class="n">下一页</a>'), html, flags=0)
        next_page_url = 'http://image.baidu.com' + \
            next_page_url[0] if next_page_url else ''
        return pic_urls, next_page_url

    def downloadPictures(self, picurls: list):
        picurls = picurls[:self.max_download_images]
        pool = ThreadPoolExecutor(max_workers=10)
        for i, picUrl in enumerate(picurls):
            try:
                pool.submit(self.downloadPic, picUrl, self.savedir +r"/baidu_{}_{}.jpg".format(self.keyword[:15], i+1))
                print('成功下载第%s张图片: %s' % (str(i + 1), str(picUrl)))
            except IOError as e:
                print('下载第%s张图片时失败: %s' % (str(i + 1), str(picUrl)))
                print(e)
                continue
