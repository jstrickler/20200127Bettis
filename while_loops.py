#!/usr/bin/env python

i = 0
while i < 3:
    print(i)
    i += 1
print("Done.")

while True:
    file_name = input("Enter FRD name or q to quit: ")
    if file_name == 'q':
        break
    if file_name == '':
        print("   -- PLEASE ENTER A FILE NAME!")
        continue
    print("Thank you. Processing", file_name + ".frd")
