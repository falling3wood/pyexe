#!/usr/bin/env python
# -*- coding:utf-8 -*-  
# ====#====#====#====
# Author: wangben
# CreatDate: 2020/9/16 17:59
# Filename:_util.py
# Function:CommontUtil工具模块编写
# ====#====#====#====
import hashlib


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
