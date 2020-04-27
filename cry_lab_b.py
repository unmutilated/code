def ReadFile(): # Define a read file operation.
    filename = input("Enter filename to encrypt make sure to designate .txt: ")
    f = open(filename, "r")
    data = f.read()
    for x in data:
        if not x.isalpha(): # Make sure that it replaces anything that is not a letter with nothing.
            data = data.replace(x, "")
    f.close()
    return data

def Permutation_And_Display_Plaintext_String():
    key = input("Please enter your key to encrypt file: ") # Your input.
    oldword = sorted(key) # Sorts your input alphabetically.
    print(oldword) # Prints alphabetically sorted input.
    wordlist = [] # Create an empty list.
    for lett in key: # For every letter in your input do:
        index = oldword.index(lett) # Create index in which each letter is counted. 
        wordlist.append(index+1) # Append to wordlist[], and add from 1 up the alphabetically sorted list.
        oldword[index] = "."  # Make it so that double letters are continually added instead of repeated.
    print("Permutation: "+ str(wordlist)) # Print the index of letters.
    ciphertext = ReadFile() 
    ciphertext.replace("\n", "") # Join any new lines as one long string.
    print("Alpha only with no spaces: " + ciphertext)

def Make_Blocks():  
    keylength=len(key)
    blocks = []
    while True: # Break the plaintext into key length blocks.
        datalength = len(ciphertext)
        if datalength != 0:
            if datalength < keylength:
                blocks.append(ciphertext[0:datalength].upper() + "Q"*(keylength - datalength)) # Pad Q"s to the last block.
                break
            else:
                blocks.append(ciphertext[0:keylength].upper())
                ciphertext = ciphertext[keylength:len(ciphertext)]
        else:
            break
    print("Blocks: " + str(blocks))

def Encrypt_Plaintext_Blocks():
    blocklist=[]
    for lett in blocks: # Re-arrange letters in each block.
        tempitem = list(lett)
        item=0
        while item < keylength:
            tempitem[wordlist[item]-1] = lett[item]
            item += 1
        blocklist.append(''.join(tempitem))
    print("Cipher blocks: " + str(blocklist))
    print(*blocklist, sep="")
