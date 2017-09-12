from bs4 import BeautifulSoup
import re
from urllib import parse
import html_outputer

class HtmlParser(object):
    
    
    def _get_new_urls(self, page_url, soup):
        new_urls = set()


        links = soup.find_all('a',href=re.compile(r"^/company/l370000-v0-p"))

        for link in links:
            new_url = link['href']
            new_full_url = parse.urljoin("https://www.cnal.com/",new_url)
            new_urls.add(new_full_url)
        return new_urls
            


    def _get_new_datas(self, page_url, soup):

        res_datas = []
        

        
        titles_node = soup.find_all(class_="cnal-company")
        contacts_node = soup.find_all(class_ = "bond-tel")
        cellphones_node = soup.find_all(class_ = "ico-text ico-mobile")
        businesses_node = soup.find_all(class_ = "zhuying")
        addresses_node = soup.find_all(class_ = "ico-text ico-add")
        while len(titles_node) > 9:          
            res_data = {}        
            res_data['contact'] = re.search(r".+",contacts_node.pop().get_text()).group()    
            res_data['phone'] = re.search(r"\d+",contacts_node.pop().get_text()).group()
            res_data['cellphone'] = re.search(r"\d+-\d+",cellphones_node.pop().parent.get_text()).group()
            res_data['business'] = re.sub(r"\s"," ",businesses_node.pop().get_text())
            res_data['address'] = re.search(r".+",addresses_node.pop().parent.get_text()).group()
            res_data['title'] = re.search(r".+",titles_node.pop().get_text()).group() 
            res_datas.append(res_data)
  
        return res_datas
    

        
    def parse(self,page_url,html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url,soup)
        new_datas = self._get_new_datas(page_url,soup)
        return new_urls,new_datas
    



