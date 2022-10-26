import classes
import sys

def exists(current_directory, file_name):
    if file_name in current_directory.hashTable:
        return True
    else:
        return False

def create(current_directory, file_name):
    exists(current_directory, file_name)
    if not exists(current_directory, file_name):
        current_directory.hashTable[file_name] = classes.File(name=file_name, content="")
    else:
        print(f"{file_name} already exists in {current_directory.path}")

def delete(current_directory, file_name):
    if exists(current_directory, file_name):
        current_directory.hashTable.pop(file_name)
    else:
        print(f"{file_name} does not exist in {current_directory.path}")
    

def Open(current_directory,file_name, mode):
    if exists(current_directory, file_name):
        if mode.upper() == "READ":
            current_directory.hashTable[file_name].read = True
        elif mode.upper() == "WRITE":
            current_directory.hashTable[file_name].write = True
        else:
            print("Mode can be either read or write")
            return False
        return current_directory.hashTable[file_name]
    else:
        print(f"{file_name} does not exist in {current_directory.path}")
        return False  
    

def Close(file):    #File exists as opened so no need to check existence
    file.read = False
    file.write = False
    return False

def mkDir(current_directory, new_directory):
    if not exists(current_directory, new_directory):
        current_directory.hashTable[new_directory] = classes.Directory(name=new_directory, hashTable=dict(), path=current_directory.path)
    else:
        print(f"{new_directory} already exists in {current_directory.path}")

def chDir(current_directory, new_directory, mode):
    if mode.upper() == "PATH":  #new_directory is full path
        directories = new_directory.split('/')
        for x in directories[2:len(directories)-1]: #Read comment for parent mode
            current_directory = current_directory.hashTable[x]
        
    elif mode.upper() == "PARENT":
        directories = new_directory.path.split('/')
        for x in directories[2:len(directories)-2]:
            #start from index 2 as first is empty (due to spliting first /) and second is home (already current directory)
            #Till len - 2 because last is empty (due to spliting last /) and second last is the original current directory
            current_directory = current_directory.hashTable[x]            

    elif mode.upper() == "CHILD":
        current_directory = current_directory.hashTable[new_directory]
    
    return current_directory

def move(current_directory, source_file, target_file):
    current_directory[target_file] = current_directory[source_file]

def printElements(current_directory):
    print(f"\n{current_directory.path}:")
    for x in current_directory.hashTable:
        print(f"    {x}")
        
def printMemoryMap(current_directory):
    print(f"\n{current_directory.path}:")
    for x in current_directory.hashTable:
        print(f"    {x} -> Starts at: {hex(id(x))} Size: {sys.getsizeof(x)} Bytes")