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

#leave only alphabets in the plaintext file
with open("marylamb.txt", "r") as myfile:
    data = myfile.read().replace('\n', '')
    
    for x in data:
        if not x.isalpha():
            data = data.replace(x, "")
myfile.close()

# break the plaintext into key length blocks
y=len(myword)
slclst = []

while True:
    z=len(data)
    if z != 0:
        if z < y:
            slclst.append(data[0:z].upper() + "Q"*(z+1))   #pad Q to the last block
            break
        else:
            slclst.append(data[0:y].upper())
            data = data[y:len(data)]
    else:
        break

print("Blocks: " + str(slclst))

# re-arrange letters in each block: permutation
blocklst=[]
for lstitem in slclst:
    tempitm = list(lstitem)
    
    i=0
    while i < y:
        tempitm[permutlst[i]-1] = lstitem[i]
        i += 1
        
    blocklst.append(''.join(tempitm))

print("Cipher blocks: " + str(blocklst))

