# -*- coding: utf-8 -*-
"""
Created on Fri May 10 21:33:24 2019

@author: qnh12
"""
#输出图片路径至txt文件

import os.path

import glob

import os

 

if __name__ == "__main__":       #主函数

    realpath = os.path.realpath(__file__)       #获取当前执行脚本的绝对路径

    dirname = os.path.dirname(realpath)       #去掉文件名，返回目录（realpath的）

    extension = 'jpg'                                        #寻找文件类型：jpg

    file_list = glob.glob('*.'+extension)             #glob.glob 获取当前工作目录下(所有.jpg结尾的文件名称，返回一个列表。）

    filetxt = open(os.path.join(dirname, 'name.txt'), 'w')  #打开一个文件，文件绝对路径是  dirname（目录）+name.txt 

    

    

    for index, filename in enumerate(file_list):    #enumerate()，列表增加索引。 用for.. in ..遍历。

       

        str_index = str(index)     #对于该索引对应的文件，记录索引名字，名字转换为字符串。

        filepath = os.path.join(dirname, filename)     # 记录绝对路径

        filetxt.write('%s\n'%(filepath))                        # 写入到文档中。打开的文件除了write()操作，还有writelines()。

        

    filetxt.close()                 #循环结束，关闭文件。
