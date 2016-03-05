def for_loop(data):
    for line in data:
        print line

def readlines():
    fd = open("test.csv", "r")
    data = fd.readlines()
    #print data
    return data

data = readlines()
for_loop(data)
