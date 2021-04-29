#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    userin = argv[1:]
    size = len(userin)
    if size is 0:
        print("{} arguments.".format(size))
    else:
        print("{} arguments:".format(size))
        for i in range(1,size+1):
            print("{:d}: {:s}".format(i,argv[i]))
