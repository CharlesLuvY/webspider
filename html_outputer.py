import pymysql



class HtmlOutputer(object):
    def __init__(self):
        self.datas = []
    
    def collect_datas(self,data):
        if data is None:
            return
        self.datas.extend(data)

    
    def output_html(self):
        connect = pymysql.Connect(
            host = 'localhost',
            port = 3306,
            user = 'root',
            passwd = 'wunai1995',
            db = 'my_db',
            charset = 'utf8'
        )
        
        cursor = connect.cursor()
        
        sql= "INSERT INTO company (company_name,contact,cellphone,phone,address,business) VALUES (%s,%s,%s,%s,%s,%s)"
        for data in self.datas:
            cursor.execute(sql,(data['title'],data['contact'],data['cellphone'],data['phone'],data['address'],data['business']))
        connect.commit()

        
        
        
        
         
        
        
        
        
        
        
        
        
        
        
        
        
        
        #with open('pp.csv','w')as csvfile:
        #        spamwriter=csv.writer(csvfile,dialect='excel')
        #        for data in self.datas:
        #            spamwriter.writerow([data['title']]+[data['contact']]+[data['phone']]+[data['cellnumber']]+[data['address'].replace(u'\xa0', u' ')]+[data['business']])
