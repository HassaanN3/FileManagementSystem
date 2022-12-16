import functions
import sys

def exec_testcases(thread_num, home_directory, current_directory, current_file):
    file = open(f"./testCases/input/input_thread{thread_num}.txt","r")
    lines = file.readlines()
    with open(f'./testCases/output/output_thread{thread_num}.txt', 'w') as sys.stdout:  #all print statements directed to file
        for i in range(len(lines)):
            #lowercase
            if "create_directory" in lines[i]:  #create in create_directory matches with create in create {filename} hence the first condition
                words = lines[i].split()    #1 = dir_name
            elif "change_directory" in lines[i]:
                words = lines[i].split()    #1 = dir_name, 2 = mode
            elif "open" in lines[i]:
                words = lines[i].split()    #1 = file_name, 2 = mode
            elif "close" in lines[i]:
                words = lines[i].split()    #1 = file_name
            elif "create" in lines[i]:
                words = lines[i].split()    #1 = file_name
            elif "delete" in lines[i]:
                words = lines[i].split()    #1 = file_name
            elif "write" in lines[i]:
                words = lines[i].split()    #1 = file_name, 2 = text
            elif "read" in lines[i]:
                words = lines[i].split()    #1 = file_name
            elif "memory" in lines[i]:
                functions.printMemoryMap(home_directory)
    file.close()    #closing file
    sys.stdout = sys.__stdout__

def read_file():
    return