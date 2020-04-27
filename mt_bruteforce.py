#1/usr/bin python3
import sys
import hashlib
import threading

alph = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&\'()*+,-./:;<=>?@"
alphblocks = ["0123456789abcdefghijkl", "mnopqrstuvwxyzABCDEFGH", "JKLMNOPQRSTUVWXYZ!\"#$", "%&\'()*+,-./:;<=>?@"]

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
                    for e in alphblocks[mynum]:
                        m = a+b+c+d+e
                        h = hashlib.md5(m.encode()).hexdigest()
                        #print("Thread {0} is trying plaintext {1}".format(mynum, m))
                        if h in hashset:
                            Output.append("Thread {0} found a hash: plaintext {1} hashes to {2}\n".format(mynum, m, h))
                            #print("Thread {0} found a hash: plaintext {1} hashes to {2}\n".format(mynum, m, h))
                            count = count + 1
                            if count >= 1000: #make 1000 and save to file
                                print("Thread {} All Done".format(mynum))
                                SaveFile(Output)
                                sys.exit()
                            
if __name__ == "__main__":
    while True:
        userchoice = input("to hash press h [Enter to quit]: ").upper()
        if userchoice.startswith("H"):
            mythreads = []
            for i in range(4):
               x = threading.Thread(target=HashFind, args=(i,))
               x.start()
               mythreads.append(x)
            for x in mythreads:
               x.join()
        else:
            sys.exit()
