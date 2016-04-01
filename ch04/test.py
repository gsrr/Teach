import string
import re

HOST = "https://www.ptt.cc"

def extract(line):
    ptn_url = 'href="(.+)"'
    ptn_title = '">(.+)<'
    obj = re.search(ptn_url, line)
    if obj != None:
        return obj.group(1)
        #fw.write(obj.group(1))
        
    obj = re.search(ptn_title, line)
    if obj != None:
        pass
        #print obj.group(1)
        #fw.write(obj.group(1))

def readNew(page):
    data = []
    fd = open(page, "r")
    rawData = fd.readlines()
    flag = 0
    for line in rawData:
        line = string.strip(line)
        if line != "":
            if "class=\"title\"" in line:
                flag = 1
                #print line
            elif flag == 1:
                flag = 0
                data.append(extract(line))
    return data
    
data_new = readNew("test.html")
last = data_db[-1]
insert = 0
for data in data_new:
    if insert == 1:
        print data , "insert"
        continue
    if data == last:
        insert = 1
    print data , "ignore"

        
