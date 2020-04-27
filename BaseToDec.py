#!/usr/bin/python
base = int(input("Please enter a base")) #enter base
number = input("please enter a number") #enter number
    #split number into a listlike state
figures = [int(i,base) for i in str(number)]

#invert oder of figures (lowest first)
figures = figures[::-1]
result = 0

#loop over all figures
for i in range(len(figures)):

#add the contirbution of the i-th figure
    result += figures[i]*base**i
print(result)
