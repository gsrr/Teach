import urllib



base = "https://www.lungteng.com.tw/englishreader/fd.aspx?vp=Files%2fHigh6125mp3%2f6125_C_LEVEL6%5cLEVEL+6+Unit+"

for i in xrange(1, 36):
    index = "%02d.mp3"%i
    url = base + index
    print index, url
    fr = urllib.urlopen(url)
    data = fr.read()
    with open(index, "w") as fw:
        fw.write(data)
