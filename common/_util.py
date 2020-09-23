#!/usr/bin/env python
# -*- coding:utf-8 -*-  
# ====#====#====#====
# Author: wangben
# CreatDate: 2020/9/16 17:59
# Filename:_util.py
# Function:CommontUtil工具模块编写
# ====#====#====#====
import hashlib
import frozen_dir
SUPER_DIR = frozen_dir.app_path()
Home = SUPER_DIR + '/img/home.ico'
Responses = SUPER_DIR + '/img/result.ico'
History_LOG = SUPER_DIR + '/img/txt_log.ico'
toast_logo = SUPER_DIR + '/img/tips.ico'
Backdrop = SUPER_DIR + '/img/bg.jpg'
log_txt = SUPER_DIR + '/log/log.txt'


def get_md5(data):
    """
    获取md5加密密文
    :param data: 明文
    :return: 加密后的密文
    """
    m = hashlib.md5()
    b = data.encode(encoding='utf-8')
    m.update(b)
    return m.hexdigest()
def get_phone(data):
    """
    校验手机号
    :param data: 手机号
    :return: 手机号长度正确
    """
    try:
        if len(data) == 11:
            return data
        else:
            return None
    except:
        return None
def args_map(user,data):
    """
    前端数据转换josn
    :param name:
    :param data:
    :return:
    """
    name = get_phone(user)
    pwd = get_md5(data)
    try:
        return {
            "name": name,
            "pwd": pwd
        }
    except:
        return None
a = "{'time': '2020_09_23_17_58_21', 'token': '7fe58b21a3f2f23df86a36b0d98520d1', 'PCtoken': '5321692786f543f5fdaa6187de67ab91', 'URL': 'https://am.alltuu.com/rest/v3/login/v0-1600855101075-0-0-40fcc2218a8623993597a9217fd281c8'}"
print(len(a))