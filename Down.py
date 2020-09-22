#!/usr/bin/env python
# -*- coding:utf-8 -*-  
# ====#====#====#====
# Author: wangben
# CreatDate: 2020/9/17 17:12
# Filename:Down.py
# Function: 下载链接
# ====#====#====#====
import threading

import xlrd
import os,sys
import requests
from  requests.packages.urllib3 import disable_warnings
requests.packages.urllib3.disable_warnings()
from you_get import common as you_get
class ReadFlie:
    def __init__(self,path):
        self.down_list(path)
    # 读取sheet页
    def Read_excelself(self,path,index=0):
        excel = xlrd.open_workbook(path)
        sheet = excel.sheets()[index]
        return sheet
    #获取总行数，将每行内容添加至列表
    def get_row(self,path,index=0):
        sheet = self.Read_excelself(path,index)
        row = sheet.nrows
        return row
    #interface
        #读取interface数据,row:行 path：文件路径 index：sheet页
    def interface(self,path,index=0):
        url_list = []
        name_list = []
        file_list = []
        sheet = self.Read_excelself(path,index) #调用获取sheet页方法，传入path(文件路径)，index(sheet页)
        for row in sheet.get_rows():
            product_column = row[2]  #链接所在列
            path_name = row[1]
            file_name = row[0]
            url1 = product_column.value
            path_text = path_name.value
            file_text = file_name.value
            url_list.append(url1)
            name_list.append(path_text)
            file_list.append(file_text)
        return url_list,name_list,file_list
    def down_list(self,path):
        url_list,name_list,file_list = self.interface(path)
        for i in range(0,len(name_list)):
            try:
                req = self.video_down(file_list[i],name_list[i],url_list[i])
                if req == 'ok':
                    print('%s下载成功'%(file_list[i]+name_list[i]))
            except:
                print('out')
    def video_down(self,file,name,url):
        path = os.path.exists('E:\\' + file)
        if path != True:
            os.mkdir('E:\\' + file)
        save_path = 'E:\\' + file+'\\'+name
        try:
            res = requests.get(url, stream=True, verify=False)
            content_length = int(res.headers['content-length'])
            if os.path.exists(save_path):
                first_byte = os.path.getsize(save_path)
            else:
                first_byte = 0
            if content_length >first_byte:
                headers = {'Range': 'bytes=%d-' % first_byte}
                res = requests.get(url, stream=True, headers=headers,verify=False)
                with open(save_path+'.mp4', "ab") as mp4:
                    for chunk in res.iter_content(chunk_size=1024):
                        if chunk:
                            first_byte +=len(chunk)
                            mp4.write(chunk)
                            mp4.flush()
                            done = int(50 * first_byte / content_length)
                            sys.stdout.write(
                                "\r[%s%s] %d%%" % ('█' * done, ' ' * (50 - done), 100 * first_byte / content_length))
                            sys.stdout.flush()
                    return 'ok'
        except Exception as e:
            return 'no'



if __name__ == '__main__':
    path = 'C:\\Users\wangben\Desktop\下載表.xlsx'
    path2= 'C:\\Users\wangben\Desktop\下载表1.xlsx'
    ReadFlie(path2)
