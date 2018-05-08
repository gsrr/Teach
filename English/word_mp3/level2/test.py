import urllib


base = "https://www.lungteng.com.tw/englishreader/fd.aspx?vp=Files%2fHigh6123mp3%2f6123+_D_LEVEL2%5cLEVEL+2++UNIT+"

for i in xrange(1, 38):
    index = "%02d.mp3"%i
    url = base + index
    print index, url
    fr = urllib.urlopen(url)
    data = fr.read()
    with open(index, "w") as fw:
        fw.write(data)
