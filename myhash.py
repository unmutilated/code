import sys
import hashlib
import threading

def ReadFile():
    f = open("CRY_Lab_02_B_hashes.txt", "r")
    ll = f.readlines()
    f.close()
    s = set()
    for l in ll:
        s.add(l.strip())
    print("Read in {0} lines from the MD5 hash file".format(len(ll)))
    return s

def SaveFile(x):
    file1 = open("Output.txt","w")
    file1.writelines(x)
    file1.close

def HashFind():
    Output = []
    hashset = ReadFile()
    alph = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&\'()*+,-./:;<=>?@"
    count = 0
    for a in alph:
        for b in alph:
            for c in alph:
                for d in alph:
                    for e in alph:
                        m = a+b+c+d+e
                        h = hashlib.md5(m.encode()).hexdigest()
                        if h in hashset:
                            Output.append("{0} Found a hash: {1} hashes to {2}\n".format(count, m, h))
                            count = count +1
                            if count >= 1000: #make 1000 and save to file
                                print("All Done")
                                SaveFile(Output)
                                sys.exit()
                            
if __name__ == "__main__":
    while True:
        userchoice = input("to hash press h [Enter to quit]: ").upper()
        if userchoice.startswith("H"):
            HashFind()
        else:
            sys.exit()
