import sys

# read(), readline, readlines()

def read():
    fd = open("test.csv", "r")
    print fd.read()

def readline():
    fd = open("test.csv", "r")
    print fd.readline()

def readlines():
    fd = open("test.csv", "r")
    print fd.readlines()

def main():
    name = sys.argv[1]
    if name == "read":
        read()
    elif name == "readline":
        readline()
    else:
        readlines()

if __name__ == "__main__":
    main()




