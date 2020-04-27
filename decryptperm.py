#!/usr/bin/env python3

myword = input("Please enter a key word: ")
permutlst = []

# sorted the encryption key word, and index it
oldword=sorted(myword)
for lett in myword:
    x = oldword.index(lett)
    permutlst.append(x+1)
    oldword[x] = "."

print("Pernutation: " + str(permutlst))

# get the cipher code file
with open("permciphertext.txt", "r") as myfile:
    data = myfile.read().replace('\n', '')
myfile.close()

# break the cipher text into key length blocks
y=len(myword)
slclst = []

z=len(data)
while z > 0:
    slclst.append(data[0:y].upper())
    data = data[y:z]
    z=len(data)
    
    
print("Cipher blocks: " + str(slclst))

# re-arrange letters in each block based on  permutation
blocklst=[]
for lstitem in slclst:
    tempitm = list(lstitem)
    
    i=0
    while i < y:
        tempitm[permutlst.index(i+1)] = lstitem[i]
        i += 1
        

    blocklst.append(''.join(tempitm))

print("Original blocks: ", blocklst)

