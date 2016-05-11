import os
import cv2
import numpy as np
import time

def mse(img1, img2):
    img = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
    err = np.sum(img1.astype("float") - img.astype("float")) ** 2
    err /= float(img1.shape[0] * img1.shape[1])
    return err

#Generate testing data
imgs = []
files = os.listdir("base")
files.sort()
for f in files:
    imgs.append(cv2.imread("base/%s"%f, 0))

imgsTest = []
files = os.listdir("img")
files.sort()
for f in files:
    print f
    imgsTest.append(cv2.imread("img/%s"%f, 0))

fw = open("test.data", "w")
for i in imgsTest:
    fw.write("0 ")
    cnt_j = 1
    for j in imgs:
        fw.write("%d:"%cnt_j + str(mse(i,j)) + " " )
        cnt_j += 1
    fw.write("\n")
fw.close()

#start to predict
cmds = [
    './svm-scale -r range1 test.data > test.scale',
    './svm-predict test.scale train.scale.model test.predict'
]
for cmd in cmds:
    os.system(cmd)

#Read the predict result
fr = open("test.predict", "r")
for line in fr.readlines():
    print line.strip(),
