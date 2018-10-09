from typing import List, Any, Union

from pip._vendor.distlib.compat import raw_input

a = [12, 11, 13, 5, 6]
i=0
j=i+1
for j in range (1, len ( a ) ):
    key = a[j]
    a[i] = a[j] - 1;
while (i > 0 and a[i] > key):
    a[i + 1] = a[i]
    i = i - 1
    a[i + 1] = key
    i=i+1;
print ( a )
