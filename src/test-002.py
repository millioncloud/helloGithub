#coding=utf-8
from string import lower
import os
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)
    
t=[1,2,3];
print(calc(*t))
extra = {'city': 'Beijing'}
person('Michael', 30, **extra);
a=(1,3,4)[0:2]
print(a)
b=[x * x for x in range(1, 11)]
print(b)
#L = ['Hello', 'World', 18, 'Apple', None]
#l= [s.lower() for s in L if isinstance(s,str) else s for s in L]
#l=[s. lower() for s in L if(isinstance(s,str)) else s for s in L]
L=['This','is','a','18','string']
print [s.upper() if (isinstance(s,str)) else s for s in L]
fruit="hello : {}, {}, and {}"
fruit.format('apple', 'pears', '123')
print("hello : {}, {}, and {}".format('apple', 'pears', '123'));
print('{:,}'.format(1234567890));
def print_seat(seat):
    for item in seat:
        print"${}".format(item)
    print"-"*15
    total=get_seat_total(seat)
    print"Total:${}".format(total)
def get_seat_total(seat):
    total=0
    for dish in seat:
        total=total+dish
    return total


seats=[[19.95],
          [20.45+3.10],
          [7/2,2.1,21.45],
          [7/2,2.1,14.99]
          ]
grand_total=0;
for seat in seats:
    print_seat(seat)
    grand_total=grand_total+get_seat_total(seat)
    print"\n"
    print"="*15
    print"Grand Total${}".format(grand_total)