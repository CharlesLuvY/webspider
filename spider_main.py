
import url_manager
import html_downloader
import html_parser
import html_outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
    
    
    def craw(self, root_url):
        self.urls.add_new_url(root_url)
        count = 1
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()

                html_cont = self.downloader.download(new_url)
                new_urls,new_datas = self.parser.parse(new_url,html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_datas(new_datas)
                print ('craw %d : %s'%(count,new_url))
                count = count + 1                
                if count == 2:
                    break

            except:
                print ('craw failed')                                 
        self.outputer.output_html()
        
if __name__ == "__main__":
    root_url = "https://www.cnal.com/company/l370000-v0-p1/"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)