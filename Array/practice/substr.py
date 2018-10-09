from pip._vendor.distlib.compat import raw_input

s = raw_input()
subs = raw_input()

count = 0
for i in range(len(s) - len(subs) + 1):
    if s[i:i+len(subs)] == subs:
        count += 1
print (count)