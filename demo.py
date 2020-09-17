
#!/usr/bin/env python
# -*- coding:utf-8 -*-  
# ====#====#====#====
# Author: wangben
# CreatDate: 2020/9/17 12:05
# Filename:demo.py
# Function:
# ====#====#====#====
from PyQt5.Qt import *
from PyQt5 import QtGui
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,800)
        self.setMinimumSize(300,300)     #登陆窗口最小尺寸
        self.UI_test()


    def UI_test(self):
        self.le_account = QLineEdit(self)
        self.le_account.move(self.width() / 2 - self.le_account.width()/2, self.height() / 2 - 50)
        # self.le_account.move(0,0)
        self.le_account.resize(200,30)
        self.le_account.setPlaceholderText('请输入账号')
        self.le_password = QLineEdit(self)
        self.le_password.move(self.width() / 2 - self.le_password.width()/2, self.height() / 2)
        self.le_password.setEchoMode(QLineEdit.Password)
        self.le_password.setPlaceholderText('请输入密码')
        self.le_password.resize(200, 30)
        self.btn = QPushButton('登陆',self)
        self.btn.resize(100,30)
        self.btn.move(self.width() / 2 -self.btn.width()/2, self.height() / 2 + 50)
        self.btn.clicked.connect(self.checkin)
        self.label = QLabel(self)
        self.label.resize(150,50)
        self.label.move(self.width()/2,self.height()/2+100)
        self.label.setText('请登陆')
        self.label.setStyleSheet('background-color:cyan')

    def resizeEvent(self, a0: QtGui.QResizeEvent):
        print(self.size())
        self.le_account.move(self.width() / 2 - self.le_account.width()/2, self.height() / 2 - 50)
        self.le_password.move(self.width() / 2 - self.le_password.width()/2, self.height() / 2)
        self.le_password.setEchoMode(QLineEdit.Password)
        self.btn.move(self.width() / 2 -self.btn.width()/2, self.height() / 2 + 50)
        self.label.move(self.width() / 2-self.label.width()/2, self.height() / 2 + 100)
        # print(self.le_account.pos())
        # print(self.le_account.size())
    def checkin(self):
        account = self.le_account.text()
        print(account)
        pwd = self.le_password.text()
        print(account)
        if account != 'abc':
            self.le_account.setText('')
            self.le_password.setText('')
            self.label.setText('账号不存在')
        elif pwd != '123':
            self.le_password.setText('')
            self.label.setText('密码错误')
        else:
            self.label.setText('登陆成功')
        self.label.adjustSize()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())