def ReadFile():
    filename = "CRY100_01_Lab_Substitution.txt"
    f = open(filename, "r")
    data = f.read()
    f.close()
    return data

def CountLetters(data):
    dict = {}
    for x in data:
        if x == ' ':
            continue
        if x in dict.keys():
            dict[x] += 1
        else:
            dict[x] = 1
    #print(dict)
    
    s = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    return s

def DecodeMsg(ciphertext, enc, plain, count):
    i = 0
    msg = ""
    for x in ciphertext:
        i += 1
        if i > count:
            break
        if x == " ":
            msg += " "
        else:
            j = enc.index(x)
            c = plain[j]
            msg += c
    return msg
    
print("SecureSet Crypto Day 1 - Lab A - Substitution Cipher")
print("Step 1 - Read Cipher Text")
print("Justin Bagdon\n")
ciphertext = ReadFile()
#print("Read {0} letters of cipher text\n".format(len(ciphertext)))
lettercount = CountLetters(ciphertext)

enc = ""
for x in lettercount:
    enc += x[0]

print("Encrypted Letters Order:")
print(enc)
plain = "ETAOSINHRLDMUCGYFWPBVKXJQZ"
print("Reference String:")
print(plain)
print(" ")
count = 200
print("Encrypted Message:")
print(ciphertext[:count],'\n')
msg = DecodeMsg(ciphertext, enc, plain, count)
print("Decoded Message:")
print(msg, '\n')
print("All Done!")
