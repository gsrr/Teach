import sys
import urllib2

def ex2():
    opener = urllib2.build_opener(urllib2.HTTPSHandler(debuglevel=1))
    opener.addheaders.append(('Cookie', 'over18=1'))
    fd = opener.open("https://www.ptt.cc/bbs/Gossiping/index.html")
    lines = fd.readlines()
    for line in lines:
        #print line
        pass

def ex1():
    fd = urllib2.urlopen("https://www.ptt.cc/bbs/Gossiping/index.html")
    lines = fd.readlines()
    for line in lines:
        print line

if __name__ == "__main__":
    func = getattr(sys.modules[__name__], sys.argv[1])
    func()
