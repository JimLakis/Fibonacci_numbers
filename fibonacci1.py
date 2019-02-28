# Simple Fibonacci numbers
# Python v3.6
# 3/7/2018

a, b = 0, 1
print(a, end = ' ')
while b < 1000:
    print(b, end = ' ')
    a, b = b, a + b
