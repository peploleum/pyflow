import sys

print('wesh')
a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a + b

try:
    x = int(input("enter "))
except:
    print('failure to parse int')
if x < 0:
    x = 0
    print('neg changed to zero')
elif x == 0:
    print('zero')
elif x == 1:
    print('one')
else:
    print('keep going')
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])
