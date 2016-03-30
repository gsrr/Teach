
import urllib
import urllib2

url = "http://gcis.nat.gov.tw/pub/cmpy/cmpyInfoListAction.do"

params = {
        "method":"query",
        "otherEnterFlag":"false",
        "useEUC":"N",
        "isShowEUC":"N",
        "queryKey":"",
        "selCmpyType":"1",
        "selQueryType":"2",
        "queryStr":"04541302",
        "brBanNo":"",
        "imageCode":"660219",
}
headers = {
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding":"gzip, deflate",
        "Accept-Language":"en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4",
        "Cache-Control":"no-cache",
        "Connection":"keep-alive",
        "Content-Length":"137",
        "Content-Type":"application/x-www-form-urlencoded",
        "Cookie":"JSESSIONID=e2606051350c58a6e661b3e0545e; __utma=64824761.210869420.1447432164.1456004396.1456028515.3; __utmz=64824761.1447432164.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _ga=GA1.3.1633022410.1457214552",
        "Host":"gcis.nat.gov.tw",
        "Origin":"https://gcis.nat.gov.tw",
        "Pragma":"no-cache",
        "Referer":"https://gcis.nat.gov.tw/pub/cmpy/cmpyInfoListAction.do",
        "Upgrade-Insecure-Requests":"1",
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36",

}
params = urllib.urlencode(params)
req = urllib2.Request(url, params, headers)
response = urllib2.urlopen(req)
data = response.read()
data = data.decode("big5").encode("utf-8")
#data = data.decode("big5")
print data

