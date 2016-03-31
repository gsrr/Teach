import string
import re

HOST = "https://www.ptt.cc"

def extract(line):
    ptn_url = 'href="(.+)"'
    ptn_title = '">(.+)<'
    obj = re.search(ptn_url, line)
    if obj != None:
        print obj.group(1)
        return obj.group(1)
        #fw.write(obj.group(1))
        
    obj = re.search(ptn_title, line)
    if obj != None:
        pass
        #print obj.group(1)
        #fw.write(obj.group(1))

def readDB(db):
    data = {}
    fr = open(db, "r")
    lines = fr.readlines()
    for line in lines:
        line = line.strip()
        data[line] = 1
    return data

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
    
data_db = readDB("db.ptt")
data_new = readNew("test_new.html")
for data in data_new:
    if data_db.has_key(data):
        print "Exist, Ignore"
    else:
        print "Not Exist, Insert"
