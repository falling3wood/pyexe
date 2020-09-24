#!/usr/bin/env python
# -*- coding:utf-8 -*-  
# ====#====#====#====
# Author: wangben
# CreatDate: 2020/9/23 16:04
# Filename:read_log.py
# Function:历史记录
# ====#====#====#====
import json
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from UI.GUI_style import log_MainWindow
from common._util import log_txt


class MY_window3(log_MainWindow,QMainWindow):
    def __init__(self):
        super(log_MainWindow, self).__init__()
        self.setupUi(self)
        self.send_txt()
    def send_txt(self):
        data = self._set_txt()
        data_list = []
        for i in data:
            data = ('    Time    : %s;'+'\n'+'   Token  : %s;'+'\n'+'PCtoken : %s;'+'\n'+'    URL   : %s'+'\n')%(i['time'],i['token'],i['PCtoken'],i['URL'])
            data_list.append(data)
            # print(data)
        self.textBrowser.setText(''.join(data_list))
    def _set_txt(self):
        with open(log_txt, 'r')as f:
            data = f.readlines()
            data_list = []
            for line in data:
                line = line.strip('\n')
                data = line.replace("'", '"')
                data_josn = json.loads(data)
                data_list.append(data_josn)
            return data_list
    def open(self):  # 被调用的类需要再编写一个open函数
        self.show()
    def shut(self):   #被调用的类需要再编写一个close函数
        self.close()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MY_window3()
    mainWindow.show()
    sys.exit(app.exec_())
# def _set_txt():
#     with open(log_txt,'r')as f:
#         data = f.readlines()
#         data_list = []
#         for line in data:
#             line = line.strip('\n')
#             data = line.replace("'", '"')
#             data_josn = json.loads(data)
#             data_list.append(data_josn)
# _set_txt()