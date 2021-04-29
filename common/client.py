import requests
import json
import allure
import time
import uuid
from hashlib import md5
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

from urllib.parse import urlencode
#  requests  加密规则

class HttpClient:
    header = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate,br",
        "Accept-Language": "zh,zh-CN;q=0.9,en-US;q=0.8,en;q=0.7",
        'cache-control': 'no-cache',
        "Content-type": "application/x-www-form-urlencoded",
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36',
    }

    @staticmethod
    def request_url(HTTP_METHOD, source, token, api_v, Host, args_map, limiting):
        """
        接口加密请求
        @param HTTP_METHOD:  接口类型  GET/POST
        @param source:  接口请求来源
        @param token:   初始 null or M-Token or Pc-Token
        @param api_v:   接口版本  0
        @param Host:    接口请求路径  hostname+path ==
        @param args_map:  参数集合
        @param limiting:  是否限流    True or False
        @return: URL请求结果
        """
        if limiting:
            Guid = str(uuid.uuid3(uuid.NAMESPACE_DNS, str(uuid.uuid1()))).replace("-", "")
            re_url = Host + '/' + HttpClient().sign_url_v4_guid(source, token, api_v, args_map, Guid)
        else:
            re_url = Host + '/' + HttpClient().sign_url_v4(source, token, api_v, args_map)
        return HttpClient().report(HTTP_METHOD, re_url, args_map),re_url

    @staticmethod
    def report(Http_Method, re_url, Args_Map):
        session = requests.session()
        session.headers = HttpClient().header
        if Http_Method == "POST":
            r = session.post(re_url, Args_Map)
        elif Http_Method == "GET":
            r = session.get(url=re_url)
        elif Http_Method == "HEAD":
            r = session.head(re_url)
        elif Http_Method == "DELETE":
            r = session.delete(re_url)
        elif Http_Method == "PUT":
            r = session.put(re_url, Args_Map)
        elif Http_Method == "OPTIONS":
            r = session.options(re_url)
        elif Http_Method == "PATCH":
            r = session.patch(re_url, Args_Map)
        else:
            return None
        return r

    @staticmethod
    def sign_url_v4_guid(source, token, api_v, args_map, guid):
        timestamp = str(int(time.time() * 1000))  # 请求发起时间戳
        std_args_map = {"from": source, "timestamp": timestamp, "token": token, "version": api_v}
        # 把标准的四个参数组成的map和非标准参数args_map合并成一个map, 用来进行签名
        if args_map is None:
            validate_map = dict(std_args_map)
        else:
            validate_map = dict(std_args_map, **args_map)
        # 把所有参数按照参数名称进行字典序升序排序
        items = sorted(validate_map.items())
        validate_string_array = [value for key, value in items]
        string_to_be_signatures = "/"
        string_to_be_signatures += "/".join(validate_string_array)
        # 对签名字符串进行md5签名
        md5_generator = md5()
        md5_generator.update(string_to_be_signatures.encode('utf-8'))
        signature_generate = md5_generator.hexdigest()
        signature_string = "v%s-%s-%s-%s-%s-%s" % (source, timestamp, token, api_v, signature_generate, guid)
        return signature_string

    @staticmethod
    def sign_url_v4(source, token, api_v, args_map):
        timestamp = str(int(time.time() * 1000))  # 请求发起时间戳
        std_args_map = {"from": source, "timestamp": timestamp, "token": token, "version": api_v}
        # 把标准的四个参数组成的map和非标准参数args_map合并成一个map, 用来进行签名
        if args_map is None:
            validate_map = dict(std_args_map)
        else:
            validate_map = dict(std_args_map, **args_map)
        # 把所有参数按照参数名称进行字典序升序排序
        items = sorted(validate_map.items())
        validate_string_array = [value for key, value in items]
        string_to_be_signatures = "/"
        string_to_be_signatures += "/".join(validate_string_array)
        # 对签名字符串进行md5签名
        md5_generator = md5()
        md5_generator.update(string_to_be_signatures.encode('utf-8'))
        signature_generate = md5_generator.hexdigest()
        signature_string = "v%s-%s-%s-%s-%s" % (source, timestamp, token, api_v, signature_generate)
        return signature_string



if __name__ == '__main__':
    HTTP_METHOD = 'post'
    source = '100101'
    token = ""
    api_v = '0'
    host = 'https://m.guituu.com/sentinel/upload'
    args_map = {"albumIdN": "3766463115", "type": ''}
    REQ = HttpClient().request_url(HTTP_METHOD, source, token, api_v, host, args_map, True)
    print(REQ)
