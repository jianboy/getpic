from contextlib import closing
import os
import sys
import logging
import requests
from getpic.libs.json_conf import JsonConf
from getpic.libs.download_progress import DownloadProgress
import argparse

class CrawlImage:
    '''base  class for crawl image'''

    def __init__(self,debug = False):
        '''init'''
        if debug:
            logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        else:
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.parser = argparse.ArgumentParser(description="getpic for builtin configs")
        self.parser.add_argument(
            "--config", default="conf/config.json", type = str, help="path to config file")
        self.parser.add_argument("--keyword",type=str,default="baidu",help="search engine")
        self.parser.add_argument("--num",type=int,default=10,help="download how many picture")
        self.sess = requests.Session()
        # 判断是否存在配置文件，否则命令行模式执行
        if not os.path.exists('conf/config.json'):
            self.keyword = sys.argv[1]
            try:
                self.max_download_images = int(sys.argv[2])
            except ValueError as e:
                self.max_download_images = 20
                logging.warning("输入的下载图片数量不是数字，默认下载20张:" + e)
            self.savedir = r"data/"
        else:
            self.jsonConf = JsonConf()
            self.conf = self.jsonConf.load()
            
            self.keyword = self.conf.get('keyword').strip()
            self.max_download_images = self.conf.get('max_download_images')
            self.savedir = self.conf.get('savedir')
            self.header = self.conf.get('headers')
            self.sess.headers.update(self.header)


    def download_pic(self, pic_url: str, file_name: str) -> None:
        '''
        download a picture
        '''
        with closing(self.sess.get(url=pic_url, stream=True, timeout=10)) as response:
            chunkSize = 1024
            contentSize = int(response.headers["content-length"])
            if(os.path.exists(file_name) and os.path.getsize(file_name) == contentSize):
                print("跳过" + file_name)
            else:
                progress = DownloadProgress(file_name, total=contentSize, unit="KB",
                                            chunk_size=chunkSize, run_status="downloading", fin_status="downloaded")
                if not os.path.exists(os.path.dirname(file_name)):
                    os.makedirs(os.path.dirname(file_name))
                with open(file_name, "wb") as file:
                    for data in response.iter_content(chunk_size=chunkSize):
                        file.write(data)
                        progress.refresh(count=len(data))

    def run(self):
        ''' run crawl image'''
        pass
