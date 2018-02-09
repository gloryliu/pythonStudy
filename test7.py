import json
import requests

class TwoColorBall:
    def __init__(self):
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
                        'Accept':'application/json, text/javascript, */*; q=0.01',
                        'Accept-Encoding':'gzip, deflate',
                        'Accept-Language':'zh-CN,zh;q=0.9',
                        'Cookie':'UniqueID=dIIaC2ArfIdbMhiu1518146248944; Sites=_21; 21_vq=7',
                        'Host':'www.cwl.gov.cn',
                        'Proxy-Connection':'keep-alive',
                        'Referer':'http://www.cwl.gov.cn/kjxx/ssq/kjgg/',
                        'X-Requested-With':'XMLHttpRequest'}
        self.debug = True

    def log(self,logInfo):
        if self.debug == True:
            print(logInfo)

    def getData(self):
        url = 'http://www.cwl.gov.cn/cwl_admin/kjxx/findDrawNotice?name=ssq&issueCount=100'
        self.log('url='+url)
        s = requests.Session()
        response = s.get(url,headers = self.headers)
        #self.log(response.text)
        self.handleData(response.text)

    def handleData(self,dataInfo):
        data_json = json.loads(dataInfo)
        array = data_json['result']
        for obj in array:
            self.anayRedBall(obj['red'])

    def anayRedBall(self,red):
        conList = []
        conListItem = []
        reds = red.split(',')
        maxItem = int(conListItem[0])

        for i in range(len(reds)):
            item = int(reds[i])
            if(item!=maxItem+1):
                conList.append(conListItem)
                
            if(i+1<=len(reds)):
                bef = int(reds[i])
                if(i+1==len(reds)):
                    after = bef
                else:
                    after = int(reds[i+1])
            if after-bef<=1:
                    conList.append(bef)
        if(len(conList)>0):
            print(red)
            print(conList)

spider = TwoColorBall()
spider.getData()
