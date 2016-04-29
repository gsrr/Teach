import os
import cv2
import numpy as np
import time

def mse(img1, img2):
    img = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
    err = np.sum(img1.astype("float") - img.astype("float")) ** 2
    err /= float(img1.shape[0] * img1.shape[1])
    return err

imgs = []
files = os.listdir("base")
files.sort()
for f in files:
    imgs.append(cv2.imread("base/%s"%f, 0))

fw = open("train.data", "w")
cnt = 0
num = 0
for i in imgs:
    if cnt == num:
        fw.write("1 ")
    else:
        fw.write("0 ")
    cnt_j = 1
    for j in imgs:
        fw.write("%d:"%(cnt_j) + str(mse(i,j)) + " " )
        cnt_j += 1
    fw.write("\n") 
    cnt += 1
    

#dataTest
imgsTest = []
files = os.listdir("database")
files.sort()
for f in files:
    print f
    imgsTest.append(cv2.imread("database/%s"%f, 0))

fw = open("test.data", "w")
print len(imgsTest)
for i in imgsTest:
    fw.write("0 ")
    cnt_j = 1
    for j in imgs:
        fw.write("%d:"%cnt_j + str(mse(i,j)) + " " )
        cnt_j += 1
    fw.write("\n")

fw.close()

print os.system("cp train.data ./model/")
print os.system("cp test.data ./model/")
