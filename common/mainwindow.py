#!/usr/bin/env python
# -*- coding:utf-8 -*-  
# ====#====#====#====
# Author: wangben
# CreatDate: 2020/9/16 12:24
# Filename:  mainwindow.py
# Function:  GUI 启动工具
# ====#====#====#====
import sys
import time

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import *
from PyQt5.uic.properties import QtGui

from UI.GUI_style import Ui_mainWindow
from common._util import *
from common.login_client import Http_Client
from common.read_log import MY_window3
from common.send_data import MY_window2


class MY_window1(Ui_mainWindow,QMainWindow):
    def __init__(self):
        super(Ui_mainWindow, self).__init__()
        self.setupUi(self)  # 这句话相当于设置控件
        self.data_main = None
        self.log_main = None
        self.init_slot()
    def init_slot(self):
        """
        初始化信号槽连接
        """
        self.send.clicked.connect(lambda: self.on_button_Click('send'))
        self.pushButton_2.clicked.connect(lambda: self.on_button_Click('log'))
    def on_button_Click(self,tag):
        """
        按钮点击事件槽函数
        :param tag: 点击的按钮的TAG
        :return: 出错返回,不执行后续操作逻辑
        """
        # 歷史記錄
        # print(tag)
        if tag == 'log':
            self.log_main = MY_window3()
            self.log_main.show()
        # 發送請求
        # print(mold)
        if tag == 'send':
            mold = self.get_text()
            if mold == None:
                self.msg_box('提示','输入参数不正确。。。')
            elif mold == 'req_out':
                self.msg_box('提示','請求失敗。。。')
            else:
                self.data_main = MY_window2()
                self.data_main.show()
    def get_text(self):
        get_host = self.input_host.text()
        get_phone = self.input_phone.text()
        get_pwd = self.input_pwd.text()
        try:
            if get_host == '' or get_phone == '' or get_pwd == '' :
                return None
            else:
                try:
                    data = args_map(get_phone,get_pwd)
                    req = self._url_report(get_host,data)
                    if req == None:
                        return 'req_out'
                except:
                    pass
                return 'ok'
        except Exception as e:
            return None
    def keyPressEvent(self, QKeyEvent):
        """
        监听键盘触发事件,通过判断是否按下的按键为Enter或者Return键
        :param QKeyEvent: 键盘触发事件
        """
        if QKeyEvent.key() == Qt.Key_Enter or QKeyEvent.key() == Qt.Key_Return:
            self.send.click()
    def _url_report(self,get_host, data):
        """
        發送請求
        :param get_host: url
        :param data: 请求数据josn
        :return: ok、None
        """
        data_time = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time()))
        try:
            req,url = Http_Client().request_url(get_host, data)
            YH_token = req.json()
            url_token = YH_token['data']['token']
            pc_token = YH_token['data']['obj']['pcToken']
            write_txt = {
                "time": data_time,
                "token": url_token,
                "PCtoken": pc_token,
                "URL":url
            }
            with open(log_txt, "a+") as file:  # 只需要将之前的”w"改为“a"即可，代表追加内容
                    file.write(str(write_txt) + "\n")
            return 'ok'
        except:
            return None
    def open(self):  # 被调用的类需要再编写一个open函数
        self.show()
    def shut(self):   #被调用的类需要再编写一个close函数
        self.close()

    def msg_box(self,title, msg):
        """提示框 """
        QMessageBox.warning(self,title, msg, QMessageBox.Yes)
if __name__ == "__main__":
        app = QApplication(sys.argv)
        mainWindow = MY_window1()
        mainWindow.show()
        sys.exit(app.exec_())


