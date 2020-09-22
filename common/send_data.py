#!/usr/bin/env python
# -*- coding:utf-8 -*-  
# ====#====#====#====
# Author: wangben
# CreatDate: 2020/9/17 14:18
# Filename:send_data.py
# Function: 按钮跳转页面
# ====#====#====#====
import sys
from datetime import time
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox,QDesktopWidget
from UI.resul import send_MainWindow
from UI.token import log_MainWindow

class Send_LOG(send_MainWindow, QMainWindow):
    def __init__(self):
        super(Send_LOG,self).__init__()
        self.setupUi(self)
        self.setWindowTitle('登录信息')
    def _report(self,pc,token,url):
        self.export_pc.setText(pc)
        self.export_token.setText(token)
        self.export_url.setText(url)
        QMessageBox.warning(self,'提示','加载中。。。。')
    # def back_button(self):
    #     self.pushButton.setCheckable(True)
        # if self.pushButton.isChecked():
            # self.pushButton.clicked.connect(main_Window.show)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = Send_LOG()
    mainWindow.show()
    sys.exit(app.exec_())