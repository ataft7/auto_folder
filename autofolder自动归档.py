#!/usr/bin/evn python
#-*- coding:utf8 -*-
# 

import os
import shutil

path = './'
dirs = os.listdir(path)
try:
    for file in dirs:
        if file[-2:] != 'py':                              #不移动脚本程序
            folder_name = path + file.split('.')[-1]       #文件夹名称设定为文件的后缀名
            if not os.path.exists(folder_name):            #判断文件夹是否存在
                os.mkdir(folder_name)                      #不存在则创建文件夹
            shutil.move(file,folder_name)              #移动文件到文件夹
            print('{} '.format(file))                  #打印结果
        else:
        #    shutil.move(file,folder_name)
            print('{} 运行完成'.format(file))
except:
    print('无文件归档或文件正在使用中！！！')

input('按任意键退出。。。')