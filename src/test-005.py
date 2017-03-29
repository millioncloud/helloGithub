#coding=utf-8
'''
Created on 2017年3月23日

@author: John
'''
from _bsddb import DB_LOCK_UPGRADE
import StudentModel
from src.StudentModel import BaseModel
import random
import os  
import datetime
import json
import mysqldb 
from fileinput import filename
def print_roster(students):
    print "students"
    for student in students:
        print "*"*15
        student.print_student()  
        

class Malestu(StudentModel.Student):
    def __init__(self,name,school,grade,addr):
        super(Malestu,self).__init__(name=name,school=school,grade=grade)
        if not addr:
            addr=raw_input("what is the addr")
        self.addr=addr
        
    def _str_(self):
        return "{name},{school},{grade},{addr}".format(name=self.name,school=self.school,grade=self.grade,addr=self.addr)        
    
    def _eq_(self,other):
        if self.name==other.name and self.addr==other.addr:
            return True
        else:
            return False
    
    def get_json(self,filename):
        try:
            f=open('savejson/'+filename)
            savejson=json.load(f)
            f.close()
        except:
            savejson={}
        return savejson
        
    def save_json(self):
        try:
            os.mkdir('savejson')
        except:
            pass
        date=datetime.datetime.now()
        filename="{Y}{M}{D}.json".format(Y=date.year,M=date.month,D=date.day)
        savejson=self.get_json(filename)
        now=datetime.datetime.now()
        key=str(now.hour)+str(now.minute)+str(now.second)
        savejson[key]=self.addr
        
        f=open('savejson/'+filename,'w')
        json.dump(savejson,f,indent=2)
        f.close()     


    
def main():

    Mstu3=Malestu("2","4","3","4")
    Mstu2=Malestu("2","4","3","4")
    #print(Mstu2._eq_(Mstu3))
    Mstu3.save_json()
main()
            