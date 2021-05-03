#!/usr/bin/python3
def uniq_add(my_list=[]):
    tot = 0
    for i in set(my_list):
        tot += i
    return tot
