#!/usr/bin/env python
# -*- coding:utf-8 -*-  
# ====#====#====#====
# Author: wangben
# CreatDate: 2020/9/24 15:59
# Filename:run.py
# Function:
# ====#====#====#====
import sys
from PyQt5.QtWidgets import QApplication
from common.mainwindow import MY_window1

if __name__ == "__main__":
        app = QApplication(sys.argv)
        mainWindow = MY_window1()
        mainWindow.show()
        sys.exit(app.exec_())