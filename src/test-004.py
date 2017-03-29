#coding=utf-8
'''
Created on 2017年3月23日

@author: John
'''

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

def main():
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
#if _name_=="_main_":
main()
