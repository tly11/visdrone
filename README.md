# visdrone 
 
## main.py
 
将annotations中txt格式的标注转换为VOC标注的.xml文件，保存在Annotations中。

## trainnamelist.py

将images文件夹内的图片随机以9：1的比例分成两部分，一个用于train，一个用于val。输出图片名的txt分别存于train.py与val.txt中，存在ImagesSets/Main中

## label.py

将.xml文件转换为yolov5所用的格式：类别 x-中心 y-中心 width height
并输出存放有图片绝对路径的txt文件于data中
train与val分别输出，需要更改label.py中所有“train”字符串


