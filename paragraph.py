#!/usr/bin/python3
import sys, os, re
from pprint import pprint as pp
''' Example
Aug 11 22:56:07 frontend01 dhclient[709]: DHCPREQUEST of 1.1.1.1 on eth0 to 172.31.1.1 port 67
Aug 11 22:56:07 frontend01 dhclient[709]: DHCPACK of 1.1.1.1 from 172.31.1.1
Aug 11 22:56:07 frontend01 dhclient[709]: bound to 1.1.1.1 -- renewal in 37000 seconds.
'''
file_ = 'paragraph.txt'
b = 'DHCPREQUEST'
c = 'bound'

def paragraph(f,begin,end):
    f = open(f, 'r').readlines()
    start_ = []
    stop_ = []
    list_par = []
    para = []
    for i,j in enumerate(f):
        if re.search(begin, j) and len(start_) == len(stop_):
            start_.append(int(i))
        if re.search(end, j) and len(stop_) < len(start_):
                stop_.append(int(i))
    if len(start_) > len(stop_):
        start_.pop(-1)
    for i,j in enumerate(start_):
        list_par.append([j,stop_[i]])
    for i in list_par:
        for j in range(i[0], i[1]+1):
            data = f[j].split('\n')[0]
            para.append(data)
    return para


pp (paragraph(file_,b,c))
