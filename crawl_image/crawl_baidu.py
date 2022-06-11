#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Contact :   liuyuqi.gov@msn.cn
@Time    :   2022/06/11 13:42:22
@License :   Copyright © 2017-2022 liuyuqi. All Rights Reserved.
@Desc    :   baidu image search
'''


from urllib.parse import quote
import re

from crawl_image.crawl_image import CrawlImage
import requests
from conf import *
import os


class CrawlImageFromBaidu( CrawlImage):
    def __init__(self, keyword="boy", max_download_images=100, savedir=r"data/baidu/"):
        super().__init__(keyword, max_download_images, savedir)

    def run(self):
        url_init = url_init_first + quote(keyword, safe='/')
        all_pic_urls = []
        page_urls, next_page_url = get_page_urls(url_init, headers)
        all_pic_urls.extend(page_urls)
        os.makedirs(savedir, exist_ok=True)
        page_count = 0  # 累计翻页数
        # if not os.path.exists('./images'):
        #     os.mkdir('./images')

    #   获取图片链接
        while True:
            page_urls, next_page_url = get_page_urls(next_page_url, headers)
            page_count += 1
            print('正在获取第%s个翻页的所有图片链接' % str(page_count))
            if next_page_url == '' and page_urls == []:
                print('已到最后一页，共计%s个翻页' % page_count)
                break
            all_pic_urls.extend(page_urls)
            if len(all_pic_urls) >= max_download_images:
                print('已达到设置的最大下载数量%s' % max_download_images)
                break

        down_pic(list(set(all_pic_urls)), max_download_images, savedir)

def get_page_urls(page_url, header):
    if not page_url:
        return [],''
    try:
        html = requests.get(page_url, headers=headers)
        html.encoding='utf-8'
        html = html.text
    except IOError as e:
        print(e)
        return [], ''
    print(html)
    pic_urls = re.findall('"objURL":"(.*?)",', html, re.S)
    print(pic_urls)
    next_page_url = re.findall(re.compile(r'<a href="(.*)" class="n">下一页</a>'), html, flags=0)
    next_page_url = 'http://image.baidu.com' + next_page_url[0] if next_page_url else ''
    return pic_urls, next_page_url


def down_pic(pic_urls, max_download_images, savedir):
    pic_urls = pic_urls[:max_download_images]
    for i, pic_url in enumerate(pic_urls):
        try:
            pic = requests.get(pic_url, timeout=15)
            imgpath = os.path.join(savedir, "baidu_fgjianzhu_{}.jpg".format(i+1))
            with open(imgpath, "wb") as f:
                f.write(pic.content)
                print('成功下载第%s张图片: %s' % (str(i + 1), str(pic_url)))
        except IOError as e:
            print('下载第%s张图片时失败: %s' % (str(i + 1), str(pic_url)))
            print(e)
            continue

