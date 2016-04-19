import urllib
import urllib2
import ssl
import os
import numpy as np
import cv2
'''
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

#1 connect web page
params = urllib.urlencode(params)
req = urllib2.Request(url, params, headers)
gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
response = urllib2.urlopen(req, context=gcontext)

#2 read header
cookie = response.info().getheader("Set-cookie").split(";")[0]
headers["Cookie"] = cookie

#3 read image code
image_url = "https://gcis.nat.gov.tw/pub/kaptcha.jpg"
req = urllib2.Request(image_url, None, headers)
gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
response = urllib2.urlopen(req, context=gcontext)
fw = open("code.jpg", "wb")
fw.write(response.read())
fw.close()
os.system("cp code.jpg ~/public_html/")
'''

#4 image processing
image = cv2.imread("code.jpg", 0)
resized_image = cv2.resize(image, (0,0), fx=3, fy=1) 
edges = cv2.Canny(image,100,200)
kernel = np.ones((2,2), np.uint8)
dilation = cv2.dilate(edges, kernel, iterations=1)

contours, hierarchy = cv2.findContours(dilation.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print len(contours)
cnt = 0
for c in contours:
    (x,y,w,h) = cv2.boundingRect(c)
    roi = dilation[y:y+h, x:x+w]
    thresh = roi.copy()
    cv2.imwrite("database/img_%d.jpg"%cnt, thresh)
    os.system("cp database/img_%d.jpg ~/public_html/"%cnt)
    cnt += 1
    '''
    if w < 100:
        if w > 15 and h > 15:
            roi = dilation[y:y+h, x:x+w]
            thresh = roi.copy()
            cv2.imwrite("database/img_%d.jpg"%cnt, thresh)
            os.system("cp database/img_%d.jpg ~/public_html/"%cnt)
            cnt += 1
    '''
