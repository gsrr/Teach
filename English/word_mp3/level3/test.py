import urllib


base = "https://www.lungteng.com.tw/englishreader/fd.aspx?vp=Files%2fHigh6124mp3%2f6124_D_LEVEL3%5cLEVEL+3+UNIT+"

for i in xrange(1, 35):
    index = "%02d.mp3"%i
    url = base + index
    print index, url
    fr = urllib.urlopen(url)
    data = fr.read()
    with open(index, "w") as fw:
        fw.write(data)
