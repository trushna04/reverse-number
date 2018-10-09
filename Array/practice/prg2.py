from array import *
from audioop import avg
from statistics import mean

from pip._vendor.distlib.compat import raw_input

n = int(input())
my_dict={}

for i in range (n):
    student_name = str(raw_input())
    marklist=[]
    for j in range(3):
        mark=int(raw_input())
        marklist.append(mark)
    a=sum(marklist)
    b=len(marklist)
    c=a/b
    my_dict[student_name]=c
    print(my_dict)
name1=str(raw_input())
print(my_dict[name1])


