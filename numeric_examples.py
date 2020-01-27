#!/usr/bin/env python

s1 = "100"

i1 = 100
i2 = 0x100
i3 = 0o100  # 0100 not allowed
i4 = 0b100

f1 = 123.456
f2 = 123.
f3 = .456
f4 = 1.2093e27

i = True
j = False

print(5 + True)
print(10 - False)
print()

c1 = 123j
c2 = 455j

a = 31
b = 13

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a ** b)  # a ^ b
print(a % b)
print()

x = 10
x += 2  # x = x + 2
x /= 3
x *= 7
print(x)

#  x++  ++x  x-- --x  NOT IN PYTHON

# x = 5
# y = x++
# z = ++x
# print(x, y, z)

# PEMDAS

data = "10/22/2019"
fields = data.split('/')
month = int(fields[0])
day = int(fields[1])
year = int(fields[2])

bad_number = "DeadBeef"

print(int(bad_number, 16))


# str()  bool()

print(hex(1000))
print(bin(1000))












