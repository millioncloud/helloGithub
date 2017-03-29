#coding=utf-8 
'''
Created on 2017年3月23日

@author: John
'''
#FIleName:Student.py
class Student(object):
    def __init__(self,name,school,grade):
        if not name:
            name=raw_input("what is the name")
        if not school:
            school=raw_input("waht is the school")
        if not grade:
            grade=self.get_grade()
            
        
        self.name=name
        self.school=school
        self.grade=grade
        
    def get_grade(self):
        while True:
            grade=raw_input("what is the grade [K,1-5]")
            if grade.lower() not in ['k','1','2','3','4','5']:
                print "error"
            else:
                return grade
    
    def print_student(self):
        print"Name:{}".format(self.name)
        print"School:{}".format(self.school)
        print"Grade:{}".format(self.grade)
        
class BaseModel():
    def _init_(self,name,age):
        self.name=name
        self.age=age
        print"baseclass is inited"
    def speak(self,name):
        print"base is spaek%s"%name
    