#!/usr/bin/env python
# -*- coding:utf-8 -*-  
# ====#====#====#====
# Author: wangben
# CreatDate: 2020/9/23 11:06
# Filename:UI_start.py
# Function: 启动页
# ====#====#====#====
import sys
from PyQt5.QtWidgets import QApplication
from common.mainwindow import *
app = QApplication(sys.argv)
# 实例化各个类
w1 = MY_window1()
w2 = MY_window2()
w3 = MY_window3()
# 将主窗口进行展示调用
w1.show()
# 主窗口发送/历史记录与子窗口1、2使用connect方法连接起来
w1.ui.send.clicked.connect(w2.open)
w1.ui.pushButton_2.clicked.connect(w3.open)
# 子窗口1关闭
w2.ui.pushButton.clicked.connect(w2.shut)
# 子窗口2关闭
w3.ui.pushButton.clicked.connect(w3.shut)
sys.exit(app.exec_())