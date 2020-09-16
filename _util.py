#!/usr/bin/env python
# -*- coding:utf-8 -*-  
# ====#====#====#====
# Author: wangben
# CreatDate: 2020/9/16 17:59
# Filename:_util.py
# Function:CommontUtil工具模块编写
# ====#====#====#====
import hashlib
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QMessageBox, QWidget


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
def args_map(name,data):
    """
    前端数据转换josn
    :param name:
    :param data:
    :return:
    """
    pwd = get_md5(data)
    return {
        "name": name,
        "pwd": pwd
    }
def hint_dialog(widget: QWidget, title: str, content: str) -> None:
    """
    display a dialog with choose button
    :param widget: the dialog rely on the father window
    :param title: the dialog title word
    :param content: the dialog content is used to hint user's
    :return: None
    """
    tip_box = QMessageBox(QMessageBox.Information, title, content)
    submit = tip_box.addButton(widget.tr('确定'), QMessageBox.YesRole)
    tip_box.setModal(True)
    tip_box.exec_()
    if tip_box.clickedButton() == submit:
        pass
    else:
        return
def accept_box(widget, title, msg):
    return QMessageBox.warning(widget, title, msg, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
def msg_box(widget, title, msg):
    QMessageBox.warning(widget, title, msg, QMessageBox.Yes)