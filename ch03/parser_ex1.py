import string

fd = open("test.html", "r")
data = fd.readlines()
flag = 0
for line in data:
    line = string.strip(line)
    if line != "":
        if "class=\"title\"" in line:
            flag = 1
            print line
        elif flag == 1:
            flag = 0
            print line


