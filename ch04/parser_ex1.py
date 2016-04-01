import string

fd = open("test.html", "r")
fw = open("test_write.html", "w")
data = fd.readlines()
flag = 0
for line in data:
    line = string.strip(line)
    if line != "":
        if "class=\"title\"" in line:
            flag = 1
            #print line
            fw.write(line)
        elif flag is 1:
            flag = 0
            #print line
            fw.write(line)

                
