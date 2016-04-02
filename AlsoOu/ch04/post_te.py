#http://stackoverflow.com/questions/27835619/ssl-certificate-verify-failed-error
import urllib
import urllib2
import ssl
import os

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
#4 input image code & query string
params = {
    "brBanNo" : "",
    "imageCode" : "",
    "isShowEUC" : "N",
    "method" : "query",
    "otherEnterFlag" : "false",
    "queryKey" : "sed6237",
    "queryStr" : "",
    "selCmpyType" : "1",
    "selQueryType" : "2",
    "useEUC" : "N"
}
query = raw_input("Enter your query string:")
code = raw_input("Enter your image code:")
params["queryStr"] = query
params["imageCode"] = code

#5 connect web page -> Get result
params = urllib.urlencode(params)
req = urllib2.Request(url, params, headers)
gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
response = urllib2.urlopen(req, context=gcontext)
data = response.read()
data = data.decode("big5").encode("utf-8")
fw = open("target.html", "w")
fw.write(data)
fw.close()



