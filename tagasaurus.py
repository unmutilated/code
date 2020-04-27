import sys
import hmac
'''
 3 -take msg and run taggen
 4 -compare tag from taggen to tag in txt file
 5 -if tags are good store results with message in good.txt
 6 -if tags are bad store results in bad.txt

'''
def ReadFile(): #1
    f = open(input("Please enter filename you wish TaGaSaUrUsReX to examine: "), "r")
    filedata = f.readlines()
    f.close()
    return filedata
def ReadKey():
    keyfile = open(input("Please Enter a KEY FILE to be used: "), "r")
    key = keyfile.read()
    keyfile.close()
    return key

messages = [] #raw messages from file
hashes = [] # raw hashes from file
GoodMessages = []
GoodHashes = []
BadMessages = []
BadHashes = []
key = ReadKey()
print(key)

def seperate_insert():
    filedata = ReadFile()
    for delimiter in filedata:
        d = delimiter.index(":")
        m = delimiter[0:d]
        h = delimiter[d + 1:].strip()
        messages.append(m)
        hashes.append(h)
        print(messages)
print(messages)
        
def gen_tag(messages, key):
    hm = hmac.new(key.encode())
    hm.update(messages.encode())
    return hm.hexdigest()
    
if __name__ == "__main__":
    while True:
        userchoice = input("press Y to examine file [Enter to quit]: ").upper()
        if userchoice.startswith("Y"):
            seperate_insert()
            t = gen_tag(messages, key)
            print(messages + ':' + t)
else:
    sys.exit()
