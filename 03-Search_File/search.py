import os

def Get_path(SearchedName):
    myDrives = ["C:\\","D:\\","E:\\","F:\\"]
    found = 0
    paths = []
    
    for drive in myDrives:
        print("searching in "+drive+"..")
        for root, dirs, files in os.walk(drive):
            if SearchedName in files or SearchedName in dirs:
                found +=1
                paths.append(root+"\\"+SearchedName)
        
    if found == 0:
        print(SearchedName+" not found on any drive\n")
    else:
        print("found "+str(found)+" times\n")
        for i in range(len(paths)):
            print("path("+str(i+1)+"): ")
            print(paths[i])
        while True:
            path = int(input("choose number of path you want to open: "))
            if path > 0 and path <= len(paths):
                os.startfile(paths[path - 1])
                break
            elif path == 0:
                print("Cancelled.")
                break
            else:
                print("Invalid choice.")



Searched = input("Enter name of file or folder to search:\n")
Get_path(Searched)