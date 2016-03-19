import string
import re

HOST = "https://www.ptt.cc"

def extract(line):
    ptn_url = 'href="(.+)"'
    ptn_title = '">(.+)<'
    obj = re.search(ptn_url, line)
    if obj != None:
        print obj.group(1)
        
    obj = re.search(ptn_title, line)
    if obj != None:
        print obj.group(1)

fd = open("test.html", "r")
data = fd.readlines()
flag = 0
for line in data:
    line = string.strip(line)
    if line != "":
        if "class=\"title\"" in line:
            flag = 1
            #print line
        elif flag == 1:
            flag = 0
            extract(line)




