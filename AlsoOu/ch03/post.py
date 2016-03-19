import urllib
import urllib2

url = "http://gcis.nat.gov.tw/pub/cmpy/cmpyInfoListAction.do"

params = {
    "brBanNo" : "",
    "imageCode" : "020189",
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
        "Cookie" : "JSESSIONID=114ba2f3080eb0353e14168f7ac2; _ga=GA1.3.1701390504.1455419117",
        "Host" : "gcis.nat.gov.tw",
        "Referer" : "https://gcis.nat.gov.tw/pub/cmpy/cmpyInfoListAction.do",
        "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0"

}
params = urllib.urlencode(params)
req = urllib2.Request(url, params, headers)
response = urllib2.urlopen(req)
data = response.read()
data = data.decode("big5").encode("utf-8")
print data

