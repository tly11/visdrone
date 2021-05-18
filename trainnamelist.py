# -*- coding: utf-8 -*-
"""
Created on Fri May 10 10:36:36 2019

@author: qnh12
"""

import os
import random


def _main():
    val_percent = 0.1
    train_percent = 0.9
    xmlfilepath = 'Annotations'
    total_xml = os.listdir(xmlfilepath)

    num = len(total_xml)
    list = range(num)
    tv = int(num * val_percent)
    tr = int(num * train_percent)
    val = random.sample(list, tv)
    train = random.sample(list, tr)

    fval = open('ImageSets/Main/val.txt', 'w')
    ftrain = open('ImageSets/Main/train.txt', 'w')


    for i in list:
        name = total_xml[i][:-4] + '\n'
        if i in val:
            fval.write(name)
        elif i in train:
            ftrain.write(name)

    ftrain.close()
    fval.close()


if __name__ == '__main__':
    _main()
