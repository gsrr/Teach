def for_loop(data):
    for line in data:
        print line.split(",")[0],
        print line.split(",")[-2]

def readlines():
    fd = open("test.csv", "r")
    data = fd.readlines()
    #print data
    return data

data = readlines()
for_loop(data)
