#!/usr/bin/python 
# -*- coding: UTF-8 -*-
import sys

print "Hello, World!";
print("你好，世界");

#raw_input("\n\nPress the enter key to continue...")

txt="这里的代码会执行么？"#Yes
print(txt)

i=0

if True:
    i=i+1
    print(i)
else:
    i=0

print(sys.argv.__len__())
print(sys.argv)