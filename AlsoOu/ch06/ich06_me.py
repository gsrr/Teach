import numpy as np
import cv2
import os
import time


#transform to gray level
'''
Grayscale is a range of shades of gray without apparent color. The darkest possible shade is black, which is the total absence of transmitted or reflected light. The lightest possible shade is white
'''
image = cv2.imread("code.jpg", 0)
cv2.imwrite("mefirst.jpg", image)
os.system("cp mefirst.jpg ~/public_html")


resized_image = cv2.resize(image, (0,0), fx=3, fy=1) 
cv2.imwrite("mefive.jpg", resized_image)
os.system("cp mefive.jpg ~/public_html/")

image = resized_image

edges = cv2.Canny(image,100,200)
cv2.imwrite("mesecond.jpg", edges)
os.system("cp mesecond.jpg ~/public_html/")


#3 dilation
kernel = np.ones((2,2), np.uint8)
dilation = cv2.dilate(edges, kernel, iterations=1)
cv2.imwrite("methird.jpg", dilation)
os.system("cp methird.jpg ~/public_html/")


#4 contour finding
contours, hierarchy = cv2.findContours(dilation.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnt = 0
for c in contours:
    (x,y,w,h) = cv2.boundingRect(c)
    if w < 100:
        if w > 15 and h > 15:
            roi = dilation[y:y+h, x:x+w]
            thresh = roi.copy()
            cv2.imwrite("mefour_%d.jpg"%cnt, thresh)
            os.system("cp mefour_%d.jpg ~/public_html/"%cnt)
            cnt += 1
