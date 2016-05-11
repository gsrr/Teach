import urllib
import urllib2
import ssl
import os
import numpy as np
import cv2
import time

cnt = 0

def mse(img1, img2):
    img = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
    err = np.sum(img1.astype("float") - img.astype("float")) ** 2
    err /= float(img1.shape[0] * img1.shape[1])
    return err

def greater(a, b):
        momA = cv2.moments(a)        
        (xa,ya) = int(momA['m10']/momA['m00']), int(momA['m01']/momA['m00'])
        momB = cv2.moments(b)        
        (xb,yb) = int(momB['m10']/momB['m00']), int(momB['m01']/momB['m00'])
        if xa > xb  :
            return 1
        elif xa == xb : 
            return 0
        else:
            return -1

def mywrite(dst, src):
    cv2.imwrite(dst, src)
    os.system( "cp %s ~/public_html/"%dst)

url = "https://gcis.nat.gov.tw/pub/cmpy/cmpyInfoListAction.do"

params = {}

headers = {
        "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Encoding" : "gzip, deflate",
        "Accept-Language" : "en-US,en;q=0.5",
        "Cache-Control" : "max-age=0",
        "Connection" : "keep-alive",
        "Cookie" : "",
        "Host" : "gcis.nat.gov.tw",
        "Referer" : "https://gcis.nat.gov.tw/pub/cmpy/cmpyInfoListAction.do",
        "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0"
}

os.system("rm -rf img")
os.system("rm -rf ~/public_html/*")
os.system("mkdir img")

#3 read image code
image_url = "https://gcis.nat.gov.tw/pub/kaptcha.jpg"
req = urllib2.Request(image_url, None, headers)
gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
response = urllib2.urlopen(req, context=gcontext)
fw = open("code.jpg","wb")
fw.write(response.read())
fw.close()

os.system("cp code.jpg ~/public_html/")
#4 image processing
image = cv2.imread("code.jpg", 0)
kernel = np.ones((2,2), np.uint8)
dilation = cv2.dilate(image, kernel, iterations=1)
resized_image = cv2.resize(dilation, (0,0), fx=3, fy=1) 
image = resized_image
edges = cv2.Canny(image,100,200)

kernel = np.ones((2,2), np.uint8)
dilation2 = cv2.dilate(edges, kernel, iterations=1)

contours, hierarchy = cv2.findContours(dilation2.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
contours.sort(greater)
database = []
for c in contours:
    (x,y,w,h) = cv2.boundingRect(c)
    if w < 100:
        if w > 15 and h > 20:
            roi = dilation2[y:y+h, x:x+w]
            thresh = roi.copy()
            database.append(thresh)
            cv2.imwrite("img/img_%d.jpg"%cnt, thresh)
            cnt += 1
            time.sleep(1)

os.system("cp -R img ~/public_html/")
