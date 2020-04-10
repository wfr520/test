import pytest,requests
from conftest import http,loggen
import allure

@allure.feature('获取学习动态')
class Teststudy:

    @allure.story('成功获取')
    def test_s(self):
        loggen.info('开始测试学习动态')
        p='api/courses/v3/trends'
        rep=http.get(path=p)
        print(rep)
        loggen.info('测试成功')