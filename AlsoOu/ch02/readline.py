def for_loop(data):
    for line in data:
        print line.split(",")[0],
        print line.split(",")[-2]

def for_loop_1(data):
    for line in data:
        str_list = line.strip().split(",")
        #print str_list
        print str_list[0], str_list[len(str_list) - 2]

def readlines():
    fd = open("test.csv", "r")
    data = fd.readlines()
    #print data
    return data

data = readlines()
for_loop_1(data)
#for_loop(data)
