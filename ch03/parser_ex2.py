import string


def extract(line):
    items = line.split("\">")
    tmp_url = items[0]
    tmp_title = items[1]
    print tmp_url.lstrip("<a href=\"")
    print tmp_title.rstrip("<\a>")
    
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




