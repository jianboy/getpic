#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Contact :   liuyuqi.gov@msn.cn
@Time    :   2024/03/19 13:57:39
@License :   Copyright © 2017-2022 liuyuqi. All Rights Reserved.
@Desc    :   
'''
from getpic.platform import CrawlImageFromBaidu
from getpic.platform import CrawlImageFromGoogle
from getpic.platform import CrawlImageFromSo
from getpic.platform import CrawlImageFromSogou
from getpic.libs.json_conf import JsonConf
import os,sys

class Getpic(object):
    
    def __init__(self):
        pass

    def run(self):
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