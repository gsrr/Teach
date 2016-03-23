
import urllib
import urllib2

url = "http://gcis.nat.gov.tw/pub/cmpy/cmpyInfoListAction.do"

params = {
    "brBanNo" : "",
    "imageCode" : "771278",
    "isShowEUC" : "N",
    "method" : "query",
    "otherEnterFlag" : "false",
    "queryKey" : "sed6237",
    "queryStr" : "04541302",
    "selCmpyType" : "1",
    "selQueryType" : "2",
    "useEUC" : "N"
}
headers = {}
params = urllib.urlencode(params)
req = urllib2.Request(url, params, headers)
response = urllib2.urlopen(req)
data = response.read()
data = data.decode("big5").encode("utf-8")
print data

