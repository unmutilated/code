import sys
import hashlib

Output = []
def ReadFile():
    file0 = open("CRY_Lab_02_B_hashes.txt", "r")
    lines = f.readlines()
    file0.close()
    s = set()
    for data in lines:
        s.add(data.strip())
    print("Read in {0} lines from the MD5 hash file".format(len(lines)))
    return s

def SaveFile():
    file1 = open("Output.txt","w")
    file1.writelines(Output)
    file1.close

def HashFind():
    hashset = ReadFile()
    alph = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&\'()*+,-./:;<=>?@"
    count = 0
    for element in range(0, len(alph)):
        m = alph[element]
        print(element) #for debuggig
        print(len(alph)) #for debugging
        h = hashlib.md5(m.encode()).hexdigest()
        if h in hashset:
            Output.append("{0} Found a hash: {1} hashes to {2}\n".format(count, m, h))
            count = count +1
            if count >= 1000:
                print("All Done")
                SaveFile()
                sys.exit()
        else:
            sys.exit()
                            
if __name__ == "__main__":
    while True:
        userchoice = input("to hash press h [Enter to quit]: ").upper()
        if userchoice.startswith("H"):
            HashFind()
        else:
            sys.exit()
                         
