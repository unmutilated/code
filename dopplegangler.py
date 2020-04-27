import os

def Get_List_of_Files(dirName):
    ListOfFile = os.listdir(dirName)
    allfiles = list()
    for entry in ListOfFile:
        fullpath = os.path.join(dirName, entry)
        if os.path.isdir(fullpath):
            allfiles = allfiles + Get_List_of_Files(fullpath)
        else:
            allfiles.append(fullpath)
    return allfiles
   
def main():
    dirName = "/home/unmutilated/Downloads/";
    listoffiles = Get_List_of_Files(dirName)
    listoffiles = list()
    for (dirpath, dirnames, filenames) in os.walk(dirName):
        listoffiles += [os.path.join(dirpath, file) for file in filenames]
        for elem in listoffiles:
            print(elem)
            
if __name__ == "__main__":
    main()
    
