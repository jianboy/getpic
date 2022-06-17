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


def main():
    '''
    --keyword "cat" --engine "google"
    '''
    # check conf/config.json is exist
    desc = '''
    ||||||||||||||||||||||||| Image Downloader ||||||||||||||||||||||||||||

        # Usage:
            1. double click to run: ImageDownloader.exe
            2。eg: use baidu to download 20 "house" pictures, please input:
                baidu 20 house

        # Cantant Us:
            Wechat: ab3255
            Mail: liuyuqi.gov@msn.cn
        
    ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    '''
    if not os.path.exists('conf/config.json'):
        # read args from command line
        if len(sys.argv) >= 3:
            engine=sys.argv[1]
            max_download_images=sys.argv[2]
            keyword=sys.argv[3]
        else:
            input("eg: baidu 20 cat")
            sys.exit(1)
    else:
        engine = JsonConf().load().get('engine')
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