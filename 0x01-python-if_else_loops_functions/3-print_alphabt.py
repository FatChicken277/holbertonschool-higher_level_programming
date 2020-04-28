#!/usr/bin/python3
for i in range(97, 122):
    if chr(i) != 'e' and chr(i) != 'q':
        print(chr(i), end='\0')
