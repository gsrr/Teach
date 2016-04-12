#Ref : https://www.youtube.com/watch?v=KESG8I9C3oA 

import numpy as np
import cv2
import os

#1 read/write image
'''
second argument is a flag which specifies the way image should be read.

cv2.IMREAD_COLOR : Loads a color image. Any transparency of image will be neglected. It is the default flag.
cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel

Note: Instead of these three flags, you can simply pass integers 1, 0 or -1 respectively.
'''
image = cv2.imread("code.jpg", 0)
cv2.imwrite("first.jpg", image)
os.system("cp first.jpg ~/public_html/")

#6 resize image
resized_image = cv2.resize(image, (100, 50))
resized_image = cv2.resize(image, (0,0), fx=3, fy=1) 
cv2.imwrite("six.jpg", resized_image)
os.system("cp six.jpg ~/public_html/")

image = resized_image
#2 edge detection
'''
cv2.Canny(image, threshold1, threshold2[, edges[, apertureSize[, L2gradient]]]) 

image - single-channel 8bit input image.
edges - output edge map; it has the same size and type as image .
threshold1 - first threshold for the hysteresis procedure.
threshold2 - second threshold for the hysteresis procedure.
apertureSize - aperture size for the Sobel() operator.

Reference:
    https://en.wikipedia.org/wiki/Image_gradient

'''
edges = cv2.Canny(image,100,200)
cv2.imwrite("second.jpg", edges)
os.system("cp second.jpg ~/public_html/")


#4 dilation
kernel = np.ones((4,4), np.uint8)
dilation = cv2.dilate(edges, kernel, iterations=1)
cv2.imwrite("four.jpg", dilation)
os.system("cp four.jpg ~/public_html/")

#3 contour finding
#reference : http://opencvpython.blogspot.tw/2012/06/hi-this-article-is-tutorial-which-try.html
#contours, hierarchy = cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
contours, hierarchy = cv2.findContours(dilation,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnt = 0
for c in contours:
    (x,y,w,h) = cv2.boundingRect(c)
    if w > 15 and h > 15:
        print (x,y,w,h)
        roi = edges[y:y+h, x:x+w]
        thresh = roi.copy()
        cv2.imwrite("five_%d.jpg"%cnt, thresh)
        os.system("cp five_%d.jpg ~/public_html/"%cnt)
        cnt += 1
    
'''

contours is a Python list of all the contours in the image. Each individual contour is a Numpy array of (x,y) coordinates of boundary points of the object.

In OpenCV 2, findContours returns just two values, contours and hierarchy. 


'''
im = cv2.imread('code.jpg')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print len(contours)
cv2.drawContours(imgray, contours, 3, (0,255,0), 3)
cv2.imwrite("third.jpg", imgray)
os.system("cp third.jpg ~/public_html/")

#7 contour finding
print
im = cv2.imread('five_3.jpg')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_CCOMP ,cv2.CHAIN_APPROX_SIMPLE)
cnt = 0
for c in contours:
    for p in c :
        print p[0]
    '''
    print c[0]    
    roi = edges[y:y+h, x:x+w]
    thresh = roi.copy()
    cv2.imwrite("seven_%d.jpg"%cnt, thresh)
    os.system("cp seven_%d.jpg ~/public_html/"%cnt)
    cnt += 1
    '''
