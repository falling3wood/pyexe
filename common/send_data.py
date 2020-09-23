#!/usr/bin/env python
# -*- coding:utf-8 -*-  
# ====#====#====#====
# Author: wangben
# CreatDate: 2020/9/17 14:18
# Filename:send_data.py
# Function: 按钮跳转页面
# ====#====#====#====
import os
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox,QDesktopWidget
from UI.GUI_style import send_MainWindow
from common._util import log_txt
import json


class MY_window2(send_MainWindow,QMainWindow):
    def __init__(self):
        super(MY_window2, self).__init__()
        self.setupUi(self)
        self.show_data()
    def show_data(self):
        a = self._read_txt()
        data = a.replace("'", '"')
        data_josn = json.loads(data)
        self.export_url.setText(data_josn['URL'])
        self.export_pc.setText(data_josn['PCtoken'])
        self.export_token.setText(data_josn['token'])
    def open(self):  # 被调用的类需要再编写一个open函数
        self.show()
    def shut(self):   #被调用的类需要再编写一个close函数
        self.close()
    def _read_txt(self):
        # with open(log_txt, 'rb') as f:  # 打开文件
        #     # 在文本文件中，没有使用b模式选项打开的文件，只允许从文件头开始,只能seek(offset,0)
        #     # first_line = f.readline()  # 取第一行
        #     offset = -223  # 设置偏移量
        #     while True:
        #         """
        #         file.seek(off, whence=0)：从文件中移动off个操作标记（文件指针），正往结束方向移动，负往开始方向移动。
        #         如果设定了whence参数，就以whence设定的起始位为准，0代表从头开始，1代表当前位置，2代表文件最末尾位置。
        #         """
        #         f.seek(offset, 2)  # seek(offset, 2)表示文件指针：从文件末尾(2)开始向前50个字符(-223)
        #         lines = f.readlines()  # 读取文件指针范围内所有行
        #         if len(lines) >= 2:  # 判断是否最后至少有两行，这样保证了最后一行是完整的
        #             last_line = lines[-1]  # 取最后一行
        #             break
        #         # 如果off为223时得到的readlines只有一行内容，那么不能保证最后一行是完整的
        #         # 所以off翻倍重新运行，直到readlines不止一行
        #         offset *= 2
        #     # print('文件' + log_txt + '第一行为：' + first_line.decode())
        #     # print('文件' + log_txt + '最后一行为：' + last_line.decode())
        #     return last_line.decode()

        filesize = os.path.getsize(log_txt)
        blocksize = 1024
        dat_file = open(log_txt, 'rb')
        last_line = ""
        if filesize > blocksize:
            maxseekpoint = (filesize // blocksize)
            dat_file.seek((maxseekpoint - 1) * blocksize)
        elif filesize:
            # maxseekpoint = blocksize % filesize
            dat_file.seek(0, 0)
        lines = dat_file.readlines()
        if lines:
            last_line = lines[-1].strip()
        # print "last line : ", last_line
        dat_file.close()
        return last_line.decode()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MY_window2()
    mainWindow.show()
    sys.exit(app.exec_())