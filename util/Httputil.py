import requests,json
from common import commonDate
class HttpUtil:
    def __init__(self):
        self.http=requests.session()
        self.headers={"Content_Type":"application/json; charset=utf-8"}
    def get(self,path):
        p = commonDate.host + path
        self.headers['token'] = commonDate.token
        rep=self.http.get(url=p,headers=self.headers)
        try:
            assert rep.json()['ok']==True
        except:
            print(rep.json()['ok'])
        self.printrep(rep)
        rep_json = rep.text
        rep_dict = json.loads(rep_json)
        return rep_dict
    def post(self,data,path):
        p=commonDate.host+path
        self.headers['token']=commonDate.token
        js=json.dumps(data)
        rep = self.http.post(url=p,data=js,headers=self.headers)
        assert rep.json()['ok'] == 200
        rep_json=rep.text
        rep_dict=json.loads(rep_json)
        return rep_dict
    def printrep(self,rep):
        print('---------http response begin   ---------------')
        print(rep.status_code)
        for k,v in rep.headers.items():
            print(f'{k}:{v}')
        print(rep.content.decode('utf8'))

        print('---------http response end    ----------------')
