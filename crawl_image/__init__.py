#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Contact :   liuyuqi.gov@msn.cn
@Time    :   2022/06/11 13:52:19
@License :   Copyright © 2017-2022 liuyuqi. All Rights Reserved.
@Desc    :   main
'''
from crawl_image.crawl_baidu import CrawlImageFromBaidu
from crawl_image.crawl_google import CrawlImageFromGoogle
from crawl_image.libs.json_conf import JsonConf


def main():
    '''
    --keyword "cat" --engine "google"
    '''
    engine = JsonConf().load().get('engine')
    if engine == 'baidu':
        crawl_image = CrawlImageFromBaidu()
    elif engine == 'google':
        crawl_image = CrawlImageFromGoogle()
    crawl_image.run()
