import functions

def exec_testcases(thread_num):
    file = open(f"./testCases/input_thread{thread_num}.txt","r")
    lines = file.readlines()
    for i in range(len(lines)):
        #call functions
        print(end="")
    file.close()

def read_file():
    return