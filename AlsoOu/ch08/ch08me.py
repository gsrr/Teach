import re


def readfile(path):
    data = []
    fr = open(path, "r")
    for line in fr.readlines():
        line = line.strip()
        if line != "":
            data.append(line)
    return data

data = readfile("./SMAC2.html")
cont = "".join(data)

#1 Extract table
ptn = "<table(.*)</table>"
searchObj = re.search(ptn, cont)
table = searchObj.group(0)

#parsing table
from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self, fw):
        HTMLParser.__init__(self)
        self.meettr = 0
        self.fw = fw

    def myprint(self, msg):
        self.fw.write(msg)

    def handle_data(self, data):
        if self.meettr == 1:
            self.myprint(data + " ")

    def handle_starttag(self, tag, attrs):
        if tag == "tr":
            self.meettr = 1
            for name,value in attrs:
                if name == "style" and value == "display:none":
                    self.meettr = 0

    def handle_endtag(self, tag):
        if tag == "tr":
            self.meettr = 0
            self.myprint("\n")

fw = open("table.data", "w")
p = MyHTMLParser(fw)
p.feed(table) 
fw.close()
