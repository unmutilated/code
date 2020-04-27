#!/usr/bin/python3
import string
blacklist='~`+=-|\}{][/'
password=input("Please enter a password: ")

for char in password:
    if char in blacklist:
        print("!!!-DENIED-!!!")
        break
else:
    print("!!!-Success-!!!")

