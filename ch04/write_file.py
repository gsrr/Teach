# -*- coding: utf-8 -*-
import string
import re

HOST = "https://www.ptt.cc"

def extract(line, fw):
    ptn_url = 'href="(.+)"'
    ptn_title = '">(.+)<'
    obj = re.search(ptn_url, line)
    if obj != None:
        #print obj.group(1)
        fw.write(obj.group(1))
    
    fw.write(",")
    obj = re.search(ptn_title, line)
    if obj != None:
        #print obj.group(1)
        fw.write(obj.group(1))
    fw.write("\n")

fd = open("test.html", "r")
fw = open("db.ptt", "w")
title = "網址,標題\n"
fw.write(title)
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
            extract(line, fw)




