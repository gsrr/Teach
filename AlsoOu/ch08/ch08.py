# -*- coding: utf-8 -*-
import re

def readfile(path):
    data = []
    fr = open(path, "r")
    for line in fr.readlines():
        line = line.strip()
        if line != "":
            data.append(line)
    return data


#1 concatenate all contents
data = readfile("SMAC2.html") 
data = "".join(data)
#print data
#print type(data)

#2 Table Extraction
table = None
ptn = "<table.+</table>"
obj = re.search(ptn, data)
if obj != None:
    #print obj.group(0)
    table = obj.group(0)

#3 Html parser
import HTMLParser 
class MyHTMLParser(HTMLParser.HTMLParser):

    def __init__(self, fw):
        HTMLParser.HTMLParser.__init__(self)
        self.meettr = 0
        self.fw = fw

    def handle_starttag(self, tag, attrs):
        #print "start:", tag
        if tag == "tr":
            self.meettr = 1
            for name,value in attrs:
                #print name, value
                if value == "display:none":
                    self.meettr = 0


    def handle_endtag(self, tag):
        if tag == "tr":
            self.meettr = 0
            #print
            self.fw.write("\n")

    def handle_data(self, data):
        if self.meettr == 1:
            #print data.strip() + ",",
            # data = data.decode("utf-8").encode("big5")
            self.fw.write(data.strip() + ",")
            
fw = open("tableData.csv", "w")
obj = MyHTMLParser(fw) #instance or object
obj.feed(table)
fw.close()

    
