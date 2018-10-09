from pip._vendor.distlib.compat import raw_input

s= str(raw_input())
print (tuple(list(s)))
list( s )= string[:5] + "k" + string[6:]
