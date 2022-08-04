#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Contact :   liuyuqi.gov@msn.cn
@Time    :   2022/06/11 13:52:19
@License :   Copyright © 2017-2022 liuyuqi. All Rights Reserved.
@Desc    :   main
'''
from getpic.crawl_baidu import CrawlImageFromBaidu
from getpic.crawl_google import CrawlImageFromGoogle
from getpic.crawl_so import CrawlImageFromSo
from getpic.crawl_sogou import CrawlImageFromSogou
from getpic.libs.json_conf import JsonConf
import os,sys

def main():
    '''
    getpic cat 20
    '''
    # check conf/config.json is exist
    desc = '''
    ||||||||||||||||||||||||| Image Downloader ||||||||||||||||||||||||||||

        # Usage:
            method 1: double click to run: ImageDownloader.exe
            method 2: eg: download 20 "cat" pictures, please input:
                getpic cat 20

        # Cantant Us:
            Wechat: ab3255
            Mail: liuyuqi.gov@msn.cn
        
    ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    '''
    print(desc)
    if not os.path.exists('conf/config.json'):
        # read args from command line
        if len(sys.argv) >= 2:
            engine="baidu"
        else:
            print("params error,eg: getpic cat 20\n")
            sys.exit(1)
    else:
        engine = JsonConf().load().get('engine')
    print(engine+"--------------------")
    if engine == 'baidu':
        crawl_image = CrawlImageFromBaidu()
    elif engine == 'google':
        crawl_image = CrawlImageFromGoogle()
    elif engine == 'sogou':
        crawl_image = CrawlImageFromSogou()
    elif engine == 'so':
        crawl_image = CrawlImageFromSo()
    crawl_image.run()


__version__ = '2022.06.13'