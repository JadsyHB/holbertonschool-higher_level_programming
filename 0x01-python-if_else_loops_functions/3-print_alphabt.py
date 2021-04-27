#!/usr/bin/python3
for i in range(ord('a'), ord('z')+1):
    if i is not (ord('e') or ord('q')):
        print('{}'.format(chr(i)), end='')
