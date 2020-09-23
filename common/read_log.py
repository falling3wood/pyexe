#!/usr/bin/env python
# -*- coding:utf-8 -*-  
# ====#====#====#====
# Author: wangben
# CreatDate: 2020/9/23 16:04
# Filename:read_log.py
# Function:历史记录
# ====#====#====#====
from PyQt5.QtWidgets import QMainWindow

from UI.GUI_style import log_MainWindow

class MY_window3(log_MainWindow,QMainWindow):
    def __init__(self):
        super(MY_window3, self).__init__()
        self.ui = log_MainWindow()
        self.ui.setupUi(self)
    def open(self):  # 被调用的类需要再编写一个open函数
        self.show()
    def shut(self):   #被调用的类需要再编写一个close函数
        self.close()