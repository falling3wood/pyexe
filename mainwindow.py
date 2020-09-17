#!/usr/bin/env python
# -*- coding:utf-8 -*-  
# ====#====#====#====
# Author: wangben
# CreatDate: 2020/9/16 12:24
# Filename:  mainwindow.py
# Function:  GUI 启动工具
# ====#====#====#====
import sys
from datetime import time

from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox,QDesktopWidget
from UI.untitled import Ui_mainWindow
from UI.resul import send_MainWindow
from UI.token import log_MainWindow
# from common._util import *
from common.send_data import Send_LOG
from common.login_client import Http_Client

class mainwindow(Ui_mainWindow,QMainWindow):
    def __init__(self,*args, **kwargs):
        super(mainwindow,self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.login_init()
        self.center()
        self.send_TAG = None
        self.log_TAG = None
    def init_slot(self):
        """信号槽初始化"""
        self.send.clicked.connect(lambda: self.btn_slot('send'))
        self.pushButton_2.clicked.connect(lambda: self.btn_slot('log'))
    def btn_slot(self,tag):
        """
        按钮点击事件槽函数
        :param tag: 点击的按钮的TAG
        :return: 出错返回,不执行后续操作逻辑
        """
    #     发送
        if tag == 'send':
            self.send_TAG = send_MainWindow()
            self.send_TAG.show()
    # 历史记录
    #     if tag == 'log':
            # self.log_TAG =
    def center(self):
        """
        窗口居中显示
        :return:
        """
        screen =QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) /2,(screen.height() - size.height()) /2)
    def login_init(self):
        """
        初始化界面UI
        :return:
        """
        self.setWindowTitle('登录数据')
        self.on_button_Click()
        self.get_text()
    def on_button_Click(self):
        self.send.setCheckable(True)
        self.pushButton_2.setCheckable(True)
        self.send.clicked.connect(self.click_send)
    def click_send(self):
        mold = self.get_text()
        if self.send.isChecked():
            if mold == None:
                self.send.clicked.connect(self.msg_box)
            else:
                self.send.clicked.connect(Send_LOG.show)
    def get_text(self):
        get_host = self.input_host.text()
        get_phone = self.input_phone.text()
        get_pwd = self.input_pwd.text()
        try:
            if get_host == '' or get_phone == '' or get_pwd == '' :
                return None
            else:
                return 'ok'
        except Exception as e:
            return None
    def msg_box(self):
        QMessageBox.warning(self,'提示','输入参数不正确。。。',QMessageBox.Yes)
    def _url_report(self,get_host, data):
        req,url = Http_Client().request_url(get_host, data)
        YH_token = req.json()
        url_token = YH_token['data']['token']
        pc_token = YH_token['data']['obj']['pcToken']
        write_txt = {
            "time":time(),
            "token":url_token,
            "PCtoken":pc_token,
            "URL":url
        }
        with open('log.txt', "a+") as file:  # 只需要将之前的”w"改为“a"即可，代表追加内容
                file.write(str(write_txt) + "\n")
        self._report(pc_token,url_token,url)






if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = mainwindow()
    mainWindow.show()
    sys.exit(app.exec_())