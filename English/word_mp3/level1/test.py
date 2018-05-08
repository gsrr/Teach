import urllib



for i in xrange(1, 35):
    index = "%02d"%i
    url = "https://www.lungteng.com.tw/englishreader/fd.aspx?vp=Files%2fHigh6123mp3%2f6123+_D_LEVEL1%5cLEVEL+1+UNIT+" + index + ".mp3"
    print url
    fr = urllib.urlopen(url)
    data = fr.read()
    with open("%s.mp3"%index, "w") as fw:
        fw.write(data)
