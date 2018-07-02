##Write a program to read through a file and print the contents of the file (line by line) all in upper case. Executing the program will look as follows:
fname = input("Please enter file name to open")

try :
    handle =  open(fname)
except :
    print("no file exist please try again")
    exit()

for line in handle :
    line = line.upper()
    print (line)