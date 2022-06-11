import requests
from crawl_image.libs.json_conf import JsonConf


class CrawlImage:
    def __init__(self):
        self.sess = requests.Session()

        self.jsonConf = JsonConf()
        self.conf = self.jsonConf.load()
        self.keyword = self.conf.get('keyword')
        self.max_download_images = self.conf.get('max_download_images')
        self.savedir = self.conf.get('savedir')
        self.header = self.conf.get('headers')
        self.sess.headers.update(self.header)

    def run(self):
        pass
