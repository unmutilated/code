#!/usr/bin/python3
import sys
inputtext=""
while(inputtext.isdigit() == False):
    inputtext = input("What is the exit code?")

print("command 1 exit code", inputtext)
sys.exit(int(inputtext))

