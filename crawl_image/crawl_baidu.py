#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Contact :   liuyuqi.gov@msn.cn
@Time    :   2022/06/11 13:42:22
@License :   Copyright © 2017-2022 liuyuqi. All Rights Reserved.
@Desc    :   baidu image search
'''
from concurrent.futures import ThreadPoolExecutor
from contextlib import closing
import re
from crawl_image.crawl_image import CrawlImage
from crawl_image import api

from crawl_image.libs.download_progress import DownloadProgress


class CrawlImageFromBaidu(CrawlImage):
    def __init__(self, keyword="boy", max_download_images=100, savedir=r"data/baidu/"):
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

    def downloadPic(self, picUrl: str,fileName: str):
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

    def downloadPictures(self, picurls: list):
        picurls = picurls[:self.max_download_images]
        pool = ThreadPoolExecutor(max_workers=10)
        for i, picUrl in enumerate(picurls):
            try:
                pool.submit(self.downloadPic, picUrl, self.savedir +r"/baidu{}.jpg".format(i+1))
                print('成功下载第%s张图片: %s' % (str(i + 1), str(picUrl)))
            except IOError as e:
                print('下载第%s张图片时失败: %s' % (str(i + 1), str(picUrl)))
                print(e)
                continue
