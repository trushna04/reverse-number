import operator
from array import *
from audioop import avg
from statistics import mean
from typing import List

from pip._vendor.distlib.compat import raw_input

n = int(input())
my_dict={}

for i in range (n):
    student_name = str(raw_input())
    mark= float(raw_input())

    my_dict[student_name]=mark

sorted_x = sorted(my_dict.items(), key=operator.itemgetter(1))


i = 1;
li = []

for key in sorted_x:

    if(i==2 or i==3):
        li.append(key);
    i += 1;
names=[]
for l in li:
    names.append(l.__getitem__(0))


n = sorted(names);

for name in n:
    print(name)
