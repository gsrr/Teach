#http://stackoverflow.com/questions/27835619/ssl-certificate-verify-failed-error
import urllib
import urllib2
import ssl

url = "https://gcis.nat.gov.tw/pub/cmpy/cmpyInfoListAction.do"

params = {
    "brBanNo" : "",
    "imageCode" : "458895",
    "isShowEUC" : "N",
    "method" : "query",
    "otherEnterFlag" : "false",
    "queryKey" : "sed6237",
    "queryStr" : "04541302",
    "selCmpyType" : "1",
    "selQueryType" : "2",
    "useEUC" : "N"
}
headers = {
        "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Encoding" : "gzip, deflate",
        "Accept-Language" : "en-US,en;q=0.5",
        "Cache-Control" : "max-age=0",
        "Connection" : "keep-alive",
        "Cookie" : "JSESSIONID=621b938194f3633aeb7fa0aa2829; _ga=GA1.3.1701390504.1455419117",
        "Host" : "gcis.nat.gov.tw",
        "Referer" : "https://gcis.nat.gov.tw/pub/cmpy/cmpyInfoListAction.do",
        "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0"
}

#1 connect web page

#2 read header
#3 read image code
#4 input image code & query string
#5 connect web page -> Get result

params = urllib.urlencode(params)
req = urllib2.Request(url, params, headers)
gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
response = urllib2.urlopen(req, context=gcontext)
data = response.read()
data = data.decode("big5").encode("utf-8")
print data

