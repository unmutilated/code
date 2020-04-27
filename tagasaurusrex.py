'''
 1 -look through txt file
    -read key file
 2 -make key value pairs of msg and of tags
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

dictionary = {} 
def make_dict():
    filedata = ReadFile()
    for x in filedata:
        i = x.index(":")
        msg = x[0:i]
        h = x[i + 1:].strip()
    
if __name__ == "__main__":
    while True:
        userchoice = input("press Y to examine file [Enter to quit]: ").upper()
        if userchoice.startswith("Y"):
            make_dict()
        else:
            sys.exit()
