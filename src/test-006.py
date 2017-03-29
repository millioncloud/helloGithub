#coding=utf-8
'''
Created on 2017年3月24日

@author: John
'''
import os
import json
import mysqldb 
#print(os.getcwd())
#print(os.listdir('D:\Workspace\python-test2\src'))
#f=open('user.txt','r+')
#line="231sadadsa"
#f.write(line)
#f.close()
#f=open('user.txt','r+')
#print(f.readlines())
#starts=os.stat('user.txt')
#print(starts.st_size)

def print_seat(seat):
    for item in seat:
        print "${}".format(item)
    print "*"*15
    total=get_seat_total(seat)
    print"Total:${}".format(total)

