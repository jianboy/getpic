from contextlib import closing
import os
import sys
import requests
from getpic.libs.json_conf import JsonConf
from getpic.libs.download_progress import DownloadProgress
import argparse

class BaseCrawlImage:
    ''' base crawl class for image '''
    
    def __init__(self):
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
            self.savedir = r"data/"
        else:
            self.jsonConf = JsonConf()
            self.conf = self.jsonConf.load()
            
            self.keyword = self.conf.get('keyword').strip()
            self.max_download_images = self.conf.get('max_download_images')
            self.savedir = self.conf.get('savedir')
            self.header = self.conf.get('headers')
            self.sess.headers.update(self.header)

    def downloadPic(self, picUrl: str, fileName: str):
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

    def run(self):
        pass
