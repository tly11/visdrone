
import xml.etree.ElementTree as ET

import pickle

import os

from os import listdir, getcwd

from os.path import join

 

sets=[('train')]

 

classes = ['ignored regions','pedestrian','people','bicycle','car','van','truck','tricycle','awning-tricycle','bus','motor','others'] # each category's name


 

def convert(size, box):

    dw = 1./(size[0])

    dh = 1./(size[1])

    x = (box[0] + box[1])/2.0 - 1

    y = (box[2] + box[3])/2.0 - 1

    w = box[1] - box[0]

    h = box[3] - box[2]

    x = round((x*dw),6)

    w = round((w*dw),6)

    y = round((y*dh),6)

    h = round((h*dh),6)

    return (x,y,w,h)

 

def convert_annotation(image_id):

    in_file = open('Annotations/%s.xml'%(image_id))

    out_file = open('labels/%s.txt'%(image_id), 'w')

    tree=ET.parse(in_file)

    root = tree.getroot()

    size = root.find('size')

    w = int(size.find('width').text)

    h = int(size.find('height').text)

 

    for obj in root.iter('object'):

        difficult = obj.find('difficult').text

        cls = obj.find('name').text

        if cls not in classes or int(difficult)==1:

            continue

        cls_id = classes.index(cls)

        xmlbox = obj.find('bndbox')

        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))

        bb = convert((w,h), b)
        
        if cls_id != 0:
	    if cls_id == 1 or cls_id == 3 or cls_id == 4 or cls_id == 5 or cls_id == 6 or cls_id == 9 :
	        out_file.write(str(0) + " " + " ".join([str(a) for a in bb]) + '\n')
	    elif cls_id == 7 or cls_id == 8 or cls_id == 10 :
	        out_file.write(str(1) + " " + " ".join([str(a) for a in bb]) + '\n')
	    elif cls_id == 2 :
	        out_file.write(str(2) + " " + " ".join([str(a) for a in bb]) + '\n')

wd = getcwd()


if not os.path.exists('labels/'):

    os.makedirs('labels/')

image_ids = open('ImageSets/Main/train.txt').read().strip().split()

list_file = open('train.txt', 'w')

for image_id in image_ids:

    list_file.write('%s/images/%s.jpg\n'%(wd, image_id))

    convert_annotation(image_id)

list_file.close()
