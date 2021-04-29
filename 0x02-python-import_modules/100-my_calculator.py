#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage:", argv[0], "<a> <operator> <b>")
        exit(1)
    
    operator = argv[2]
    f = {"+": add, "-": sub, "*": mul, "/": div}
    if operator not in f:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    b = int(argv[2])
    print("{:d} {:s} {:d} = {:d}".format(a, op, b, f[op](a, b)))
