import sys
import hashlib
import threading
alph = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&\'()*+,-./:;<=>?@"
alphchunks = ['0123456789abcdefghijkl', 'mnopqrstuvwxyzABCDEFGH', 'JKLMNOPQRSTUVWXYZ!', '\"#$%&\'()*+,-./:;<=>?@']

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

def HashFind(mynum):
    Output = []
    hashset = ReadFile()
    count = 0
    for a in alph:
        for b in alph:
            for c in alph:
                for d in alph:
                    for e in alphchunks[mynum]:
                        m = a+b+c+d+e
                        h = hashlib.md5(m.encode()).hexdigest()
                        if h in hashset:
                            Output.append("{0} Found a hash: {1} hashes to {2}\n".format(count, m, h))
                            count = count +1
                            if count >= 250: #make 1000 and save to file
                                print("All Done")
                                SaveFile(Output)
                            
if __name__ == "__main__":
    while True:
        userchoice = input("to hash press h [Enter to quit]: ").upper()
        if userchoice.startswith("H"):
            mythreads = []
            for i in range(4):
                x = threading.Thread(target=HashFind, args=(i,))
                x.start()
                mythreads.append(x)
            for i in range(4):
                mythreads[i].join()
        else:
            sys.exit()
