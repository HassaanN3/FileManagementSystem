import pickle
import classes
import functions

if __name__ == '__main__':
    home_directory = classes.Directory(name='home', hashTable=dict(), path="/")
    current_directory = home_directory
    current_file = ""

    for j in range(1,4):
        functions.mkDir(current_directory, "folder_" + str(j))
        for i in range(1,6):
            functions.create(current_directory, "file_" + str(i) + ".txt")
        current_directory = functions.chDir(current_directory, 'folder_' + str(j), mode = 'child')
        
    with open('test.dat', 'wb') as file:
        pickle.dump(home_directory.hashTable, file)