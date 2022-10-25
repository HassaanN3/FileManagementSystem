#TODO create files in system
import classes
import functions
import os
import pickle

def loadFromDat():
    with open('sample.dat', 'rb') as file:
        try:
            loaded_dict=pickle.load(file)
        except EOFError:
            loaded_dict = dict()
    return loaded_dict

def saveInDat(home_directory):
    with open('sample.dat', 'wb') as file:
        pickle.dump(home_directory.hashTable, file)

if __name__ == '__main__':
    home_directory = classes.Directory(name='home', hashTable=loadFromDat(), path="")
    current_directory = home_directory
    current_file = ""

    while(1):
        print("\tFile Management System\n")
        print(f"Current Directory: {current_directory.path}")
        user_input = int(input("\n1. Create File\t2. Delete File\n3. Open File\t4. List all files\n5. Clear Screen\n6. Save and Exit\n: "))

        if user_input == 1: #Create File
            file_name = input("\nEnter File Name\n: ")
            functions.create(current_directory, file_name)

        elif user_input == 2: #Delete File
            file_name = input("\nEnter File Name\n: ")    #TODO file does not exist
            functions.delete(current_directory, file_name)

        elif user_input == 3: #Open File
            file_name = input("\nEnter File Name\n: ")    #TODO file does not exist
            mode = input("\nEnter Mode\n: ")
            current_file = functions.Open(current_directory, file_name, mode.upper())

            if current_file != False:   #Valid Parameters
                os.system('clear')

                while(1):
                    print(f"\nCurrent File: {current_directory.path}{file_name}")
                    user_input = int(input("\n1. Write in File\t2. Read from File\n3. Close File\n: "))

                    if user_input == 1: #Write in File
                        user_input = int(input("\n1. Append Mode\t2. Write at Index\n: "))
                        content = input("Enter text to write: ")

                        if user_input == 1: #Write in Append Mode
                            current_file.writeToFile(text=content)

                        elif user_input == 2: #Write at Index
                            write_at = int(input("Enter index: "))
                            current_file.writeToFile(text=content, index=write_at)

                    elif user_input == 2:   #Read from File
                        user_input = int(input("\n1. Sequential Read\t2. Read from Index\n: "))

                        if user_input == 1: #Read in Sequential 
                            print("Content: ")
                            current_file.readFromFile()
                        elif user_input == 2:   #Read from Index
                            read_from = int(input("Enter index: "))
                            
                            user_input = int(input("\n1. Read All\t2. Read x characters\n: "))
                            print("Content: ")

                            if user_input == 1: #Read all
                                current_file.readFromFile(index = read_from)

                            elif user_input == 2:   #Read x characters
                                read_size = int(input("Enter Number of Characters to Read: "))
                                current_file.readFromFile(index = read_from, size = read_size) 

                            elif user_input == 3:   #Close
                                current_file = functions.Close(current_file)
                                break

        elif user_input == 4:   #List all files in directory
            functions.printElements(current_directory)

        elif user_input == 5:   #Clear Screen
            os.system('clear')

        elif user_input == 6:   #Save in .Dat File
            saveInDat(home_directory)
            break
        
        print("\n")
