import pytest,requests
from common import commonDate
from util.Httputil import HttpUtil
from common.loggen import Loggen
loggen=Loggen('alphaCoding测试').getlog()
http=HttpUtil()
@pytest.fixture(scope="session",autouse=True)
def login():
    loggen.info('开始登录')
    pay_load = {"loginId": "20171405113", "password": "123456", "orgId": 10}
    path = commonDate.host + 'api/auth/login'
    rep = http.http.post(path, pay_load)
    http.printrep(rep)
    commonDate.token=rep.json()['data']['auth_token']
    print('登陆成功.....')
    loggen.info('登录成功')
