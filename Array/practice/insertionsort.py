from typing import List, Any, Union

from pip._vendor.distlib.compat import raw_input
n= int(raw_input())
a= []
e=0
for i in range (n):
    b=int(raw_input())
    a.append(b)
for e in range (len ( a ) ):
    for j in range (e+1, len ( a ) ):
        if(a[e]>a[j]):
            key=a[j]
            a[j]=a[e]
            a[e]=key


print ( a )

