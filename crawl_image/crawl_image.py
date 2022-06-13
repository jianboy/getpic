from contextlib import closing
from crawl_image.libs.download_progress import DownloadProgress
import requests,os
from crawl_image.libs.json_conf import JsonConf


class CrawlImage:
    def __init__(self):
        self.sess = requests.Session()

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
