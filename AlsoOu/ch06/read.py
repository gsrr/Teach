import cv2
import numpy as np
img = cv2.imread("code.jpg")
b,g,r = cv2.split(img)
img_f = cv2.imread("first.jpg")
err = np.sum(img.astype("float") - img_f.astype("float")) ** 2
err /= float(img.shape[0] * img.shape[1])
print err

#same image
img_f = cv2.imread("code.jpg")
err = np.sum(img.astype("float") - img_f.astype("float")) ** 2
err /= float(img.shape[0] * img.shape[1])
print err

#number image
img = cv2.imread("five_7.jpg")
print img.shape[0], img.shape[1]
for i in range(2,8):
    img_f = cv2.imread("five_%d.jpg"%i)
    img_rf = cv2.resize(img_f, (img.shape[1], img.shape[0]))
    err = np.sum(img.astype("float") - img_rf.astype("float")) ** 2
    err /= float(img.shape[0] * img.shape[1])
    print "five_%d"%i, err
'''
#1 read binary(gray)
fr = open("first.jpg", "rb")
print ord(fr.read(1))
print ord(fr.read(1))
print ord(fr.read(1))
print ord(fr.read(1))
print ord(fr.read(1))
print ord(fr.read(1))

print
#2 read binary(colorful)
fr = open("code.jpg", "rb")
print ord(fr.read(1))
print ord(fr.read(1))
print ord(fr.read(1))
print ord(fr.read(1))
print ord(fr.read(1))
print ord(fr.read(1))
'''
