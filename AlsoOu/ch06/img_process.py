import cv2  #opencv
import numpy as np
import os

#1 gray image
image = cv2.imread("code.jpg", 0) 
cv2.imwrite("c06first.jpg", image)
os.system("cp c06first.jpg ~/public_html")

#2 edge detection
edges = cv2.Canny(image,100,200)
cv2.imwrite("c06second.jpg", edges)
os.system("cp c06second.jpg ~/public_html/")

#3 dilation
kernel = np.ones((2,2), np.uint8)
dilation = cv2.dilate(edges, kernel, iterations=1)
cv2.imwrite("c06third.jpg", dilation)
os.system("cp c06third.jpg ~/public_html/")

#4 contour finding
contours, hierarchy = cv2.findContours(dilation.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnt = 0
print len(contours)
for c in contours:
    (x,y,w,h) = cv2.boundingRect(c)
    roi = dilation[y:y+h, x:x+w]
    thresh = roi.copy()
    cv2.imwrite("c06four_%d.jpg"%cnt, thresh)
    os.system("cp c06four_%d.jpg ~/public_html/"%cnt)
    cnt += 1

