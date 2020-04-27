import sys
import hashlib

def ReadFile():
    f = open("CRY_Lab_02_B_hashes.txt", "r")
    ll = f.readlines()
    f.close()
    s = set()
    for l in ll:
        s.add(l.strip())
    print("Read in {0} lines from the MD5 hash file".format(len(ll)))
    return s

hashset = ReadFile()

alph = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&\'()*+,-./:;<=>?@"

count = 0
msg = ""
for a in alph:
    for b in alph:
        for c in alph:
            for d in alph:
                for e in alph:
                    m = a+b+c+d+e
                    h = hashlib.md5(m.encode()).hexdigest()
                   # print(h)
                    if h in hashset:
                        print("{0} Found a hash: {1} hashes to {2}".format(count, m, h))
                        count = count +1
                        if count >= 10: #make 1000 and save to file
                            print("All Done")
                            sys.exit()
