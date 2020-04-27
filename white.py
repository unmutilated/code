#!/usr/bin/python3

whitelist='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*()'
password=input("Please enter a password: ")

for char in password:
    if char not in whitelist:
        print("!!!-DENIED-!!!")
        break
else:
    print("!!!-Success-!!!")

