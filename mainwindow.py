#!/usr/bin/env python
# -*- coding:utf-8 -*-  
# ====#====#====#====
# Author: wangben
# CreatDate: 2020/9/16 12:24
# Filename:  mainwindow.py
# Function:  GUI 启动工具
# ====#====#====#====
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox,QWidget
from UI.untitled import Ui_mainWindow
from common._util import *

class mainwindow(Ui_mainWindow,QMainWindow):
    def __init__(self,*args, **kwargs):
        super(mainwindow,self).__init__(*args, **kwargs)
        self.setupUi(self)
    def login_init(self):
        """
        初始化界面UI
        :return:
        """
        self.setWindowTitle('获取登录信息')
        self.send.setProperty('class','')
        self.pushButton_2.setProperty('class','')



if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = mainwindow()
    mainWindow.show()
    sys.exit(app.exec_())