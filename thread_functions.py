import functions
import sys

def exec_testcases(thread_num):
    file = open(f"./testCases/input/input_thread{thread_num}.txt","r")
    lines = file.readlines()
    with open(f'./testCases/output/output_thread{thread_num}.txt', 'w') as sys.stdout:  #all print statements directed to file
        for i in range(len(lines)):
            #call functions
            print(lines[i],end="")
    file.close()    #closing file
    sys.stdout = sys.__stdout__

def read_file():
    return