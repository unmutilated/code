import sys

def ReadFile():
    ReadFile = input("Enter file name to encrypt/decrypt 'Example.txt': ")
    f = open(ReadFile, "r")
    data = f.read()
    for x in data:
        if not x.isalpha(): # Make sure that it replaces anything that is not a letter with nothing.
            data = data.replace(x, "")
    f.close()
    return data
  
def Encrypt():
    key = input("Please enter your key to encrypt file: ") # Your input.
    sorted_key = sorted(key) # Sorts your input alphabetically.
    #print("Sorted Key: " + str(sorted_key)) # Prints alphabetically sorted input.
    permutation = [] # Create an empty list.
    for lett in key: # For every letter in your input do:
        index = sorted_key.index(lett) # Create variable index in which each letter is counted. 
        permutation.append(index) # Append to permutation[].
        sorted_key[index] = "."  # Make it so that double letters are continually added instead of repeated.
    #print("Permutation: "+ str(permutation)) # Print the index of letters.
    plain_text = ReadFile() # Create variable plain_text
    plain_text.replace("\n", "") # Join any new lines as one long string.
    print("PlainText: " + plain_text) # Prints the plaintext.
    print()
    keylength=len(key) # Creates variable keylength.
    plain_text_length = len(plain_text) # Creates variable plain_text_length.
    if plain_text_length == "": # If your text is nothing then exit program. 
        sys.exit()
    blocks = [] # Create a list called blocks.
    plain_text = plain_text + 'Q'*(keylength-(plain_text_length%keylength)) # Pad plain text string with Q's to length of blocks 
    plain_text_length = len(plain_text) # Re institute variable plain_text_length because length changes. 
    numblocks = plain_text_length // keylength # Create variable numblocks which is the total number of blocks you will use. 
    for i in range(numblocks): 
        blocks.append(plain_text[i*keylength:(i+1)*keylength].upper())
    #print("Plaintext_Blocks: " + str(blocks))
    ciphertext=[]
    for block in blocks:
        for num in permutation:
            ciphertext.append(block[num])
    print("Encrypted Text: ", *ciphertext, sep="")
    print()

def Decrypt():   
    key = input("Please enter your key to encrypt file: ") # Your input.
    sorted_key = sorted(key) # Sorts your input alphabetically.
    #print("Sorted Key: " + str(sorted_key)) # Prints alphabetically sorted input.
    permutation = [] # Create an empty list.
    for lett in sorted_key: # For every letter in your input do:
        index = key.index(lett) # Create variable index in which each letter is counted. 
        key = key.replace(lett, '.', 1) # Make it so that double letters are continually added instead of repeated.
        permutation.append(index) # Append to permutation[].
    #print("The permutation: ", permutation) # Print the index of letters.
    plain_text = ReadFile() # Create variable plain_text
    plain_text.replace("\n", "") # Join any new lines as one long string.
    print("PlainText: " + plain_text) # Prints the plaintext.
    print()
    keylength=len(key) # Creates variable keylength.
    plain_text_length = len(plain_text) # Creates variable plain_text_length.
    if plain_text_length == "": # If your text is nothing then exit program. 
        sys.exit()
    blocks = [] # Create a list called blocks.
    numblocks = plain_text_length // keylength # Create variable numblocks which is the total number of blocks you will use. 
    for i in range(numblocks): 
        blocks.append(plain_text[i*keylength:(i+1)*keylength].upper())
    #print("Plaintext_Blocks: " + str(blocks))
    ciphertext=[]
    for block in blocks:
        for num in permutation:
            ciphertext.append(block[num])
    print("Encrypted Text: ", *ciphertext, sep="")
    print()
    
if __name__ == "__main__":
    while True:
        userchoice = input("Encrypt or Decrypt [Enter to quit]? ").upper()
        if userchoice.startswith("E"):
            Encrypt()
        elif userchoice.startswith("D"):
            Decrypt()
        else:
            sys.exit()
