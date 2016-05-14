import urllib
import urllib2
import ssl
import os
import numpy as np
import cv2
import time

cnt = 0

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
for i in range(10): 
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

    #1 read image code
    image_url = "https://gcis.nat.gov.tw/pub/kaptcha.jpg"
    req = urllib2.Request(image_url, None, headers)
    gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    response = urllib2.urlopen(req, context=gcontext)
    fw = open("code.jpg", "wb")
    fw.write(response.read())
    fw.close()

    #2 read image
    image = cv2.imread("code.jpg", 0)

    kernel = np.ones((2,2), np.uint8)
    dilation = cv2.dilate(image, kernel, iterations=1)

    resized_image = cv2.resize(dilation, (0,0), fx=3, fy=1)

    edges = cv2.Canny(resized_image,100,200)

    kernel = np.ones((2,2), np.uint8)
    dilation = cv2.dilate(edges, kernel, iterations=1)

    contours, hierarchy = cv2.findContours(dilation.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    contours.sort(greater)
    cnt = 0

    for c in contours:
        (x,y,w,h) = cv2.boundingRect(c)
        if w < 100:
            if w > 15 and h > 20 :
                roi = dilation[y:y+h, x:x+w]
                thresh = roi.copy()
                cv2.imwrite("code_%d%d.jpg"%(i,cnt), thresh)
                os.system("cp code_%d%d.jpg ~/public_html/"%(i, cnt))
                cnt += 1

