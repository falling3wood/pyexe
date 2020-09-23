
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

# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.resize(500,800)
#         self.setMinimumSize(300,300)     #登陆窗口最小尺寸
#         self.UI_test()
#
#
#     def UI_test(self):
#         self.le_account = QLineEdit(self)
#         self.le_account.move(self.width() / 2 - self.le_account.width()/2, self.height() / 2 - 50)
#         # self.le_account.move(0,0)
#         self.le_account.resize(200,30)
#         self.le_account.setPlaceholderText('请输入账号')
#         self.le_password = QLineEdit(self)
#         self.le_password.move(self.width() / 2 - self.le_password.width()/2, self.height() / 2)
#         self.le_password.setEchoMode(QLineEdit.Password)
#         self.le_password.setPlaceholderText('请输入密码')
#         self.le_password.resize(200, 30)
#         self.btn = QPushButton('登陆',self)
#         self.btn.resize(100,30)
#         self.btn.move(self.width() / 2 -self.btn.width()/2, self.height() / 2 + 50)
#         self.btn.clicked.connect(self.checkin)
#         self.label = QLabel(self)
#         self.label.resize(150,50)
#         self.label.move(self.width()/2,self.height()/2+100)
#         self.label.setText('请登陆')
#         self.label.setStyleSheet('background-color:cyan')
#
#     def resizeEvent(self, a0: QtGui.QResizeEvent):
#         print(self.size())
#         self.le_account.move(self.width() / 2 - self.le_account.width()/2, self.height() / 2 - 50)
#         self.le_password.move(self.width() / 2 - self.le_password.width()/2, self.height() / 2)
#         self.le_password.setEchoMode(QLineEdit.Password)
#         self.btn.move(self.width() / 2 -self.btn.width()/2, self.height() / 2 + 50)
#         self.label.move(self.width() / 2-self.label.width()/2, self.height() / 2 + 100)
#         # print(self.le_account.pos())
#         # print(self.le_account.size())
#     def checkin(self):
#         account = self.le_account.text()
#         print(account)
#         pwd = self.le_password.text()
#         print(account)
#         if account != 'abc':
#             self.le_account.setText('')
#             self.le_password.setText('')
#             self.label.setText('账号不存在')
#         elif pwd != '123':
#             self.le_password.setText('')
#             self.label.setText('密码错误')
#         else:
#             self.label.setText('登陆成功')
#         self.label.adjustSize()
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = Window()
#     window.show()
#     sys.exit(app.exec_())

# import sys
# from PyQt5.QtCore import pyqtSignal
# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
#
#
# class one(QMainWindow):
#     sig_1 = pyqtSignal()
#
#     def __init__(self):
#         super(one, self).__init__()
#         self.init_ui()
#
#     def init_ui(self):
#         self.resize(300, 200)
#         self.setWindowTitle('1')
#         self.btn_1 = QPushButton(self)
#         self.btn_1.setText('Emit')
#         self.btn_1.setGeometry(100, 80, 100, 40)
#         self.btn_1.clicked.connect(self.slot_btn_1)
#         self.sig_1.connect(self.sig_1_slot)
#
#     def slot_btn_1(self):
#         self.sig_1.emit()
#
#     def sig_1_slot(self):
#         self.t = two()
#         self.t.show()
#
#
# class two(QMainWindow):
#
#     def __init__(self):
#         super(two, self).__init__()
#         self.resize(500, 100)
#         self.setWindowTitle('two')
#
#
# def ui_main():
#     app = QApplication(sys.argv)
#     w = one()
#     w.show()
#     sys.exit(app.exec_())
#
#
# if __name__ == '__main__':
#     ui_main()
# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QButtonGroup, QFrame, QToolButton, QStackedLayout,\
#     QWidget, QStatusBar
#
# import sys
#
#
# class Demo(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.__setup_ui__()
#
#     def __setup_ui__(self):
#         self.setWindowTitle("测试")
#         #窗口大小
#         self.resize(1400,800)
#         # 工具栏
#         self.frame_tool = QFrame(self)
#         self.frame_tool.setObjectName("frame_tool")
#         self.frame_tool.setGeometry(0, 0, self.width(), 25)
#         self.frame_tool.setStyleSheet("border-color: rgb(0, 0, 0);")
#         self.frame_tool.setFrameShape(QFrame.Panel)
#         self.frame_tool.setFrameShadow(QFrame.Raised)
#
#         # 1.1 界面1按钮
#         self.window1_btn = QToolButton(self.frame_tool)
#         self.window1_btn.setCheckable(True)
#         self.window1_btn.setText("window1")
#         self.window1_btn.setObjectName("menu_btn")
#         self.window1_btn.resize(100, 25)
#         self.window1_btn.clicked.connect(self.click_window1)
#         self.window1_btn.setAutoRaise(True)
#
#         # 1.2 界面2按钮
#         self.window2_btn = QToolButton(self.frame_tool)
#         self.window2_btn.setCheckable(True)
#         self.window2_btn.setText("window2")
#         self.window2_btn.setObjectName("menu_btn")
#         self.window2_btn.resize(100, 25)
#         self.window2_btn.move(self.window1_btn.width(), 0)
#         self.window2_btn.clicked.connect(self.click_window2)
#         self.window2_btn.setAutoRaise(True)
#
#         self.btn_group = QButtonGroup(self.frame_tool)
#         self.btn_group.addButton(self.window1_btn, 1)
#         self.btn_group.addButton(self.window2_btn, 2)
#
#         # 2. 工作区域
#         self.main_frame = QFrame(self)
#         self.main_frame.setGeometry(0, 25, self.width(), self.height() - self.frame_tool.height())
#         # self.main_frame.setStyleSheet("background-color: rgb(65, 95, 255)")
#
#         # 创建堆叠布局
#         self.stacked_layout = QStackedLayout(self.main_frame)
#
#         # 第一个布局界面
#         self.main_frame1 = QMainWindow()
#         self.frame1_bar = QStatusBar()
#         self.frame1_bar.setObjectName("frame1_bar")
#         self.main_frame1.setStatusBar(self.frame1_bar)
#         self.frame1_bar.showMessage("欢迎进入frame1")
#
#         rom_frame = QFrame(self.main_frame1)
#         rom_frame.setGeometry(0, 0 , self.width(), self.main_frame.height() - 25)
#         rom_frame.setFrameShape(QFrame.Panel)
#         rom_frame.setFrameShadow(QFrame.Raised)
#
#         frame1_bar_frame = QFrame(self.main_frame1)
#         frame1_bar_frame.setGeometry(0, self.main_frame.height(), self.width(), 25)
#
#         # 第二个布局界面
#         self.main_frame2 = QMainWindow()
#         self.frame2_bar = QStatusBar()
#         self.frame2_bar.setObjectName("frame2_bar")
#         self.main_frame2.setStatusBar(self.frame2_bar)
#         self.frame2_bar.showMessage("欢迎进入frame2")
#
#         custom_frame = QFrame(self.main_frame2)
#         custom_frame.setGeometry(0, 0 , self.width(), self.main_frame.height() - 25)
#         custom_frame.setFrameShape(QFrame.Panel)
#         custom_frame.setFrameShadow(QFrame.Raised)
#
#         frame2_bar_frame = QFrame(self.main_frame2)
#         frame2_bar_frame.setGeometry(0, self.main_frame.height(), self.width(), 25)
#
#         # 把两个布局界面放进去
#         self.stacked_layout.addWidget(self.main_frame1)
#         self.stacked_layout.addWidget(self.main_frame2)
#
#     def click_window1(self):
#         if self.stacked_layout.currentIndex() != 0:
#             self.stacked_layout.setCurrentIndex(0)
#             self.frame1_bar.showMessage("欢迎进入frame1")
#
#     def click_window2(self):
#         if self.stacked_layout.currentIndex() != 1:
#             self.stacked_layout.setCurrentIndex(1)
#             self.frame2_bar.showMessage("欢迎进入frame2")
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = Demo()
#     window.show()
#     sys.exit(app.exec_())
# 主窗口
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 180, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 180, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "打开窗口1"))
        self.pushButton_2.setText(_translate("MainWindow", "打开窗口2 "))


# 窗口1
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(140, 100, 54, 12))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "这是窗口1"))


# 窗口2

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(140, 140, 54, 12))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "这是窗口2"))


# 主程序
class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.window2 = Ui_Dialog()
        self.window2.setupUi()
        self.window3 = Ui_Form()
        self.window3.setupUi()
        self.pushButton.clicked.connect(self.window2.show)  # 绑定窗口2
        self.pushButton_2.clicked.connect(self.window3.show)  # 绑定窗口3


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())