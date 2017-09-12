
from urllib import request 



class HtmlDownloader(object):
    
    
    def download(self,url):

        if url is None:
            return None
        else:
            
   
            with request.urlopen(url) as response:

                data = response.read()
                return data
    



