import classes

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
        if mode == "READ":
            current_directory.hashTable[file_name].read = True
        elif mode == "WRITE":
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
    current_directory.hashTable[new_directory] = classes.Directory(name=new_directory, hashTable=dict(), path=current_directory.path)

"""def chDir(current_directory, new_directory):
    current_directory = current_directory[new_directory]

def move(current_directory, source_file, target_file):
    current_directory[target_file] = current_directory[source_file]"""

def printElements(current_directory):
    print(f"\n{current_directory.path}:")
    for x in current_directory.hashTable:
        print(f"    {x}")