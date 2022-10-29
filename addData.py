import pickle
import classes
import functions
import string
import random

if __name__ == '__main__':
    home_directory = classes.Directory(name='home', hashTable=dict(), path="/")
    current_directory = home_directory
    current_file = ""

    for j in range(1,4):
        functions.mkDir(current_directory, "folder_" + str(j))
        for i in range(1,6):
            functions.create(current_directory, "file_" + str(i) + ".txt")
            current_file = functions.Open(current_directory,"file_" + str(i) + ".txt", mode='write')
            current_file.writeToFile(text=''.join(random.choices(string.ascii_uppercase + string.digits, k=random.randrange(100))))
            current_file = functions.Close(current_file)
        current_directory = functions.chDir(current_directory, 'folder_' + str(j), mode = 'child')
        
    with open('sample.dat', 'wb') as file:
        pickle.dump(home_directory.hashTable, file)