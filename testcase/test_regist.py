#!/usr/bin/python3
import json
import re
import pymysql
import pytest
import requests

from common.yaml_utils import read_yaml_testcase, write_yaml


class TestRegist:
    def test_sendVerificationCode(self):
        url = "https://demo.api.asiatic.online/xwapi/portal-api/mp/system/sendVerificationCode"
        data = {
            "mallId": "1626111817634648066",
            "mobileNo": "15087654321"
        }

        res = requests.get(url=url, params=data)
        print(res)
        pattern = re.compile(r'"validateKey":"(.*?)"')
        print(pattern)# r的意思是不转义，即\表示原样的\
        validateKey = re.findall(pattern, res.text)  # 获取所有的('validateKey',
        print(validateKey)
        # for i in extract_value:
        #     print(i)
        #     print(i[1])  # 获取验证码key



        write_yaml("extract.yaml",validateKey)
        # pattern = re.compile(r'"(mobileNo)":"(.*?)"')  # r的意思是不转义，即\表示原样的\
        # mobileNo = re.findall(pattern, res.text)
        # write_yaml("extract.yaml", mobileNo)

        # # 打开数据库连接
        # db = pymysql.connect(host='10.0.8.41',
        #                      user='root',
        #                      password='Aic@2020',
        #                      database='sharding_as_communication')
        #
        # # 使用 cursor() 方法创建一个游标对象 cursor
        # cursor = db.cursor()
        # # 使用 execute()  方法执行 SQL 查询
        # cursor.execute(
        #     "SELECT send_content FROM sharding_as_communication.communication_log_2023 WHERE receive_account like '%15089414758%'order by id desc limit 1;")
        # # 使用 fetchone() 方法获取单条数据.
        # data = cursor.fetchone()
        # code = re.findall(r'[0-9]+', str(data))[0]
        # print(code)
        # extract_value3 = {"validateCode": res.json()["validateCode"]}
        # write_yaml("/extract.yaml", extract_value3)
        # # 关闭数据库连接
        # db.close()


    @pytest.mark.parametrize("caseinfo",read_yaml_testcase("regist.yaml"))
    def test_regist(self,caseinfo):
        method = caseinfo["request"]["menoth"]
        urls = caseinfo["request"]["url"]
        params = caseinfo["request"]["parmas"]
        res = requests.request(method=method, url=urls, json=params)
        print(res.json())


if __name__ == '__main__':
    pytest.main()