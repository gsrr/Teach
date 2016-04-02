import urllib2
import ssl
params = {}
headers = {}
image_url = "https://gcis.nat.gov.tw/pub/kaptcha.jpg"
req = urllib2.Request(image_url, params, headers)
gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
response = urllib2.urlopen(req, context=gcontext)
