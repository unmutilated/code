def ReadFile(): # Define a read file operation.
    filename = input("Enter filename to decrypt make sure to designate .txt: ")
    f = open(filename, "r")
    data = f.read()
    f.close()
    return data

#STEP 1) Alphebatize a string of characters.
key = input("Please enter your key to encrypt file: ") # Your input.
oldword = sorted(key) # Sorts your input alphabetically.
print(oldword) # Prints alphabetically sorted input.

#STEP 2) Take the alphabetized string and create a list of numbers that correspond to the string.
wordlist = [] # Create an empty list.
for lett in key: # For every letter in your input do:
    index = oldword.index(lett) # Create index in which each letter is counted. 
    wordlist.append(index+1) # Append to wordlist[], and add from 1 up the alphabetically sorted list.
    oldword[index] = "."  # Make it so that double letters are continually added instead of repeated.
print("Permutation: "+ str(wordlist)) # Print the index of letters.

#STEP 3) Read file as 1 long string of letters

ciphertext = ReadFile() 
ciphertext.replace("\n", "") # Join any new lines as one long string.
print("Alpha only with no spaces: " + ciphertext)

#STEP 4) Re-arrange the letters in a block according to the new index.

keylength=len(key)
blocks = []
datalength = len(ciphertext)
while datalength > 0: # Break the ciphertext into key length blocks.
    blocks.append(ciphertext[0:datalength].upper())
    ciphertext = ciphertext[keylength:datalength]
    datalength = len(ciphertext)
print("Blocks: " + str(blocks))

blocklist=[]
for lett in blocks: # Re-arrange letters in each block.
    tempitem = list(lett)
    item=0
    while item < keylength:
        tempitem[wordlist.index(item+1)] = lett[item]
        item += 1
    blocklist.append(''.join(tempitem))
print("Cipher blocks: ", blocks)
