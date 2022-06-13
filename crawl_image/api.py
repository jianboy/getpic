#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Contact :   liuyuqi.gov@msn.cn
@Time    :   2022/06/11 13:47:24
@License :   Copyright © 2017-2022 liuyuqi. All Rights Reserved.
@Desc    :   api interface
'''
# baidu
baidu_search_image = r"http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word="

# google
google_serach_image=r"https://www.google.com/search?q=%s&tbm=isch"


# so
so_host=r"https://image.so.com/"
so_search_image=r"https://image.so.com/j?callback=jQuery183028769737744873414_1655094505325&q=%E7%BE%8E%E5%A5%B3&qtag=&pd=1&pn=60&correct=%E7%BE%8E%E5%A5%B3&adstar=0&tab=all&sid=8499b4c02249a5d86b570ed71c0eea37&ras=1&cn=0&gn=0&kn=50&crn=0&bxn=20&cuben=0&pornn=0&manun=0&src=srp&sn=130&ps=96&pc=96&_=1655094561112"
# so_search_image=r"https://image.so.com/zjl?ch=%s&sn=%s&list=%s"

# sogou
sogou_host=r"http://pic.sogou.com"
sogou_setBigImage = r"http://pb.sogou.com/cl.gif?uigs_productid=pic&ua=Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F102.0.5005.63%20Safari%2F537.36%20Edg%2F102.0.1245.39&pagetype=searchlist_page&type=filter_module&stype=filter_bigsize&_t=1655086816719&_r=741&uigs_st=0"
sogou_getImage="http://pic.sogou.com/napi/pc/searchList?mode=2&start=%d&xml_len=48&query=%s"