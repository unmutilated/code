#!/usr/bin/python3
choose = int(input("please enter one of the following numbers:" '\n'  "(1): Encrypt" '\n' "(2): Decrypt" '\n' "ENTER: "))
if choose == 1: # if user entered 1 run this script
    def crypt(encrypt):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # define alphabet
        word = input("What is the word to encrypt? ").upper() #turn input into uppercase as variable word
        newletter = "" #place to store newletters before printing it
        newword = "" #place to store newword

        for letter in word: #as there is a letter in word variable do this:
            newletter = alphabet[(alphabet.find(letter) + 3) % 26]
                #find letter in alphabet and count up 3 from each then wrap to beginning
            newword += newletter #add newletters +3 each time to newword
        print(word, newword) #print original word next to encrypted word
    crypt("encrypt")

elif choose == 2:# if user chose decrypt run this script
    def crypt(decrypt):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        word = input("What is the word to Decrypt? ").upper()
        newletter = ""
        newword = ""
        for letter in word:
            newletter = alphabet[(alphabet.find(letter) -3) % 26]
                #find letter in alphabet and -3 each time
            newword += newletter
        print(word, newword)
    crypt("decrypt")

else:
    print("Ah, ah, ah, You didn't say the Magic Word!")



