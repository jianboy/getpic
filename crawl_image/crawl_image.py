import requests
from crawl_image.libs.json_conf import JsonConf

class CrawlImage:
    def __init__(self, keyword:str, max_download_images, savedir):
        self.sess = requests.Session()
        
        self.jsonConf = JsonConf()
        self.conf = self.jsonConf.load()
        self.keyword = self.conf.get('keyword')
        self.max_download_images = self.conf.get('max_download_images')
        self.savedir = self.conf.get('savedir')
        self.page_url = self.conf.get('url_init_first') % self.keyword
        self.header = self.conf.get('headers')

    def run(self):
        pass