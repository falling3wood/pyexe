#!/usr/bin/env python
# -*- coding:utf-8 -*-  
# ====#====#====#====
# Author: wangben
# CreatDate: 2020/9/17 12:18
# Filename:aniu.py
# Function:
# ====#====#====#====
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
#
# class Form(QDialog):
#     def __init__(self,parent=None):
#         super(Form, self).__init__(parent)
#
#         #垂直布局
#         layout=QVBoxLayout()
#
#         #创建按钮1
#         self.btn1=QPushButton('Button1')
#         #setCheckable()：设置按钮是否已经被选中，如果为True，则表示按钮将保持已点击和释放状态
#         self.btn1.setCheckable(True)
#         #toggle()：在按钮状态之间进行切换
#         self.btn1.toggle()
#         #点击信号与槽函数进行连接，这一步实现：在控制台输出被点击的按钮
#         self.btn1.clicked.connect(lambda :self.whichbtn(self.btn1))
#         #点击信号与槽函数进行连接，实现的目的：输入安妞的当前状态，按下还是释放
#         self.btn1.clicked.connect(self.btnstate)
#
#         #添加控件到布局中
#         layout.addWidget(self.btn1)
#
#         #创建按钮2
#         self.btn2=QPushButton('image')
#         #为按钮2添加图标
#         self.btn2.setIcon(QIcon(QPixmap('E:\pyqt5快速开发与实战\第四章\images\python.png')))
#         ##点击信号与槽函数进行连接，这一步实现：在控制台输出被点击的按钮
#         self.btn2.clicked.connect(lambda :self.whichbtn(self.btn2))
#
#         layout.addWidget(self.btn2)
#
#         self.btn3=QPushButton('Disabled')
#         #setEnabled()设置按钮是否可以使用，当设置为False的时候，按钮变成不可用状态，点击它不会发射信号
#         self.btn3.setEnabled(False)
#
#         layout.addWidget(self.btn3)
#
#         #创建按钮并添加快捷键
#         self.btn4=QPushButton('&Download')
#         #setDefault()：设置按钮的默认状态
#         self.btn4.setDefault(True)
#         ##点击信号与槽函数进行连接，这一步实现：在控制台输出被点击的按钮
#         self.btn4.clicked.connect(lambda :self.whichbtn(self.btn4))
#
#         layout.addWidget(self.btn4)
#
#         self.setWindowTitle("Button demo")
#         self.setLayout(layout)
#
#     def btnstate(self):
#         #isChecked()：判断按钮的状态，返回值为True或False
#         if self.btn1.isChecked():
#             print('button pressed')
#         else:
#             print('button released')
#
#     def whichbtn(self,btn):
#         #输出被点击的按钮
#         print('clicked button is '+btn.text())
# if __name__ == '__main__':
#     app=QApplication(sys.argv)
#     btnDemo=Form()
#     btnDemo.show()
#     sys.exit(app.exec_())
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, \
    QPushButton, QLineEdit, QMenuBar, QStatusBar
from PyQt5.QtCore import *

#
# class FirstWindow(QWidget):
#
#     def __init__(self, parent=None):
#         # super这个用法是调用父类的构造函数
#         # parent=None表示默认没有父Widget，如果指定父亲Widget，则调用之
#         super(FirstWindow, self).__init__(parent)
#         self.setGeometry(500, 500, 500, 500)
#         self.setWindowTitle('显示')
#
#         self.btn = QPushButton(self)
#         self.btn.setText('标定')
#         self.btn.move(150, 50)
#
# class Ui_MainWindow(object):
#     def setupUi(self, MainWindow):
#         MainWindow.setObjectName("MainWindow")
#         MainWindow.resize(624, 479)
#         self.centralwidget = QtWidgets.QWidget(MainWindow)
#         self.centralwidget.setObjectName("centralwidget")
#         self.label = QtWidgets.QLabel(self.centralwidget)
#         self.label.setGeometry(QtCore.QRect(190, 130, 51, 31))
#         self.label.setObjectName("label")
#         self.pushButton = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton.setGeometry(QtCore.QRect(330, 260, 75, 23))
#         self.pushButton.setObjectName("pushButton")
#         self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
#         self.lineEdit.setGeometry(QtCore.QRect(280, 130, 151, 21))
#         self.lineEdit.setObjectName("lineEdit")
#         self.label_2 = QtWidgets.QLabel(self.centralwidget)
#         self.label_2.setGeometry(QtCore.QRect(190, 180, 51, 31))
#         self.label_2.setObjectName("label_2")
#         self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
#         self.lineEdit_2.setGeometry(QtCore.QRect(280, 190, 151, 21))
#         self.lineEdit_2.setObjectName("lineEdit_2")
#         self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton_2.setGeometry(QtCore.QRect(200, 260, 75, 23))
#         self.pushButton_2.setObjectName("pushButton_2")
#         MainWindow.setCentralWidget(self.centralwidget)
#         self.menubar = QtWidgets.QMenuBar(MainWindow)
#         self.menubar.setGeometry(QtCore.QRect(0, 0, 624, 23))
#         self.menubar.setObjectName("menubar")
#         MainWindow.setMenuBar(self.menubar)
#         self.statusbar = QtWidgets.QStatusBar(MainWindow)
#         self.statusbar.setObjectName("statusbar")
#         MainWindow.setStatusBar(self.statusbar)
#
#         self.retranslateUi(MainWindow)
#         QtCore.QMetaObject.connectSlotsByName(MainWindow)
#
#     def retranslateUi(self, MainWindow):
#         _translate = QtCore.QCoreApplication.translate
#         MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
#         self.label.setText(_translate("MainWindow", "  长"))
#         self.pushButton.setText(_translate("MainWindow", "确定"))
#         self.label_2.setText(_translate("MainWindow", "  宽"))
#         self.pushButton_2.setText(_translate("MainWindow", "取消"))
#
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     MainWindow = QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#
#     ex = FirstWindow()
#     ex.btn.clicked.connect(MainWindow.show)
#     ex.show()
#
#     sys.exit(app.exec_())
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QLabel, QLineEdit, QPushButton
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTextEdit, QTextBrowser, QHBoxLayout, QVBoxLayout
import time


class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.iniUI()
        self.buttonClicked()

    def iniUI(self):
        self.setWindowTitle("PythonGUI教程")
        self.statusBar().showMessage("文本状态栏")
        self.resize(400, 300)
        # self.browser_label = QLabel('QTextBrowser', self)
        # self.text_edit = QTextEdit(self)
        self.text_browser = QTextBrowser(self)
        self.text_browser.move(160, 30)
        self.text_browser.resize(200, 200)
        self.qle = QLineEdit(self)
        self.qle.move(20, 80)
        btn1 = QPushButton("确定", self)
        btn1.move(20, 120)
        # print(qle.text())
        btn1.clicked.connect(self.buttonClicked)

        # 创建一个菜单栏
        menu = self.menuBar()
        # 创建两个个菜单
        file_menu = menu.addMenu("文件")
        file_menu.addSeparator()
        edit_menu = menu.addMenu('修改')

        # 创建一个行为
        new_action = QAction('新的文件', self)
        # 更新状态栏文本
        new_action.setStatusTip('打开新的文件')
        # 添加一个行为到菜单
        file_menu.addAction(new_action)

        # 创建退出行为
        exit_action = QAction('退出', self)
        # 退出操作
        exit_action.setStatusTip("点击退出应用程序")
        # 点击关闭程序
        exit_action.triggered.connect(self.close)
        # 设置退出快捷键
        exit_action.setShortcut('Ctrl+z')
        # 添加退出行为到菜单上
        file_menu.addAction(exit_action)

    def buttonClicked(self):
        self.text_browser.setText(self.qle.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(app.exec_())